#!/usr/bin/env python3
"""Publish one visual asset, inferring its URL from context."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

ROOT = Path(os.environ.get("VISUAL_EXPLAINER_ROOT", str(Path.home() / "public/explainers")))
BASE_URL = os.environ.get("VISUAL_EXPLAINER_BASE_URL", "https://canvas.krasnoperov.me/explainers").rstrip("/")


def slugify(value: str, *, allow_fallback: bool = False) -> str:
    original = value
    value = re.sub(r"[^a-z0-9._-]+", "-", value.lower().strip())
    value = re.sub(r"-{2,}", "-", value).strip("-.")
    if not value or value in {"auth", "robots.txt"}:
        if allow_fallback:
            return f"asset-{hashlib.sha256(original.encode()).hexdigest()[:10]}"
        raise ValueError("slug must contain letters or numbers and cannot be reserved")
    return value


def infer_collection() -> str | None:
    override = os.environ.get("VISUAL_EXPLAINER_COLLECTION")
    if override:
        return slugify(override)
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip():
        return slugify(Path(result.stdout.strip()).name)
    return None


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def same_file(source: Path, target: Path) -> bool:
    return target.is_file() and source.stat().st_size == target.stat().st_size and digest(source) == digest(target)


def make_readable(target: Path) -> None:
    if target.is_dir():
        for directory, _, filenames in os.walk(target):
            Path(directory).chmod(0o755)
            for filename in filenames:
                (Path(directory) / filename).chmod(0o644)
    else:
        target.chmod(0o644)


def publish(source: Path, collection: str | None, slug: str | None, replace: bool) -> str:
    source = source.expanduser().absolute()
    if not source.exists():
        raise ValueError(f"source does not exist: {source}")
    if source.is_symlink() or (source.is_dir() and any(path.is_symlink() for path in source.rglob("*"))):
        raise ValueError("refusing to publish symlinks")
    source = source.resolve()

    selected_collection = slugify(collection) if collection else infer_collection()
    parent = ROOT / selected_collection if selected_collection else ROOT
    base = slugify(slug or (source.stem if source.is_file() else source.name), allow_fallback=True)
    target = parent / (f"{base}{source.suffix.lower()}" if source.is_file() else base)
    target.parent.mkdir(parents=True, exist_ok=True)
    ROOT.chmod(0o755)
    current = target.parent
    while current != ROOT.parent:
        current.chmod(0o755)
        if current == ROOT:
            break
        current = current.parent

    if target.exists() and not replace:
        if not (source.is_file() and same_file(source, target)):
            stamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
            target = target.with_name(f"{target.stem}-{stamp}{target.suffix}")

    if source.is_dir():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, ignore=shutil.ignore_patterns(".DS_Store", ".git"))
        make_readable(target)
        entry = target / "index.html"
        if not entry.exists():
            print("warning: directory has no index.html; its file listing will be shown", file=sys.stderr)
            entry = target
    else:
        temporary = target.with_name(f".{target.name}.tmp")
        shutil.copy2(source, temporary)
        temporary.chmod(0o644)
        temporary.replace(target)
        entry = target

    relative = entry.relative_to(ROOT).as_posix()
    suffix = "/" if entry.is_dir() else ""
    return f"{BASE_URL}/{quote(relative, safe='/._-')}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish one private visual asset")
    parser.add_argument("source")
    parser.add_argument("--collection", help=argparse.SUPPRESS)
    parser.add_argument("--slug", help=argparse.SUPPRESS)
    parser.add_argument("--replace", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    print(publish(Path(args.source), args.collection, args.slug, args.replace))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        raise SystemExit(str(error)) from error
