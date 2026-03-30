#!/usr/bin/env python3
"""Fetch Gemini CLI docs from llms.txt (all-in-one format)."""

from __future__ import annotations

import hashlib
import json
import os
import re
import ssl
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import certifi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "sources.json"
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "docs_manifest.json"

USER_AGENT = "gemini-cli-docs-mirror/1.0"

# Match markdown section headers like "# Title" or "## Title"
SECTION_HEADER_REGEX = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)

REQUEST_TIMEOUT_SECONDS = 60
MAX_RETRIES = 4
BASE_BACKOFF_SECONDS = 1.5
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


@dataclass(frozen=True)
class Source:
    source_id: str
    llms_txt: str
    output_subdir: str


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_sources(config_path: Path) -> List[Source]:
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    raw_sources = payload.get("sources", [])
    if not raw_sources:
        raise RuntimeError("No sources configured in config/sources.json")

    result: List[Source] = []
    for raw in raw_sources:
        source_id = raw.get("id")
        llms_txt = raw.get("llms_txt")
        output_subdir = raw.get("output_subdir")
        if not source_id or not llms_txt or not output_subdir:
            raise RuntimeError(f"Invalid source entry: {raw}")
        result.append(
            Source(
                source_id=source_id,
                llms_txt=llms_txt,
                output_subdir=output_subdir,
            )
        )
    return result


def fetch_text(url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/markdown,text/plain,*/*"})
        try:
            with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS, context=SSL_CONTEXT) as response:
                raw = response.read()
            return raw.decode("utf-8")
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_seconds)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def sha256_text(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_existing_manifest(path: Path) -> Dict:
    if not path.exists():
        return {"files": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def clean_title(title: str) -> str:
    """Remove markdown links and URLs from title."""
    # Remove markdown links: [text](url) -> text
    title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
    # Remove URLs
    title = re.sub(r'https?://\S+', '', title)
    return title.strip()


def sanitize_filename(name: str) -> str:
    """Convert title to safe filename."""
    # Remove markdown links and URLs first
    name = clean_title(name)
    # Replace spaces and special chars with hyphens
    sanitized = re.sub(r"[^\w\s-]", "", name.lower())
    sanitized = re.sub(r"[\s]+", "-", sanitized)
    sanitized = re.sub(r"-+", "-", sanitized).strip("-")
    return sanitized or "untitled"


def extract_sections(content: str) -> List[tuple[str, str]]:
    """
    Extract sections from all-in-one llms.txt format.
    Returns list of (title, content) tuples.
    """
    sections = []
    lines = content.split("\n")
    current_title = None
    current_lines: List[str] = []

    for line in lines:
        header_match = SECTION_HEADER_REGEX.match(line)
        if header_match:
            # Save previous section if exists
            if current_title is not None and current_lines:
                section_content = "\n".join(current_lines).strip()
                if section_content:
                    sections.append((current_title, section_content))

            # Start new section
            current_title = header_match.group(2).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    # Don't forget the last section
    if current_title is not None and current_lines:
        section_content = "\n".join(current_lines).strip()
        if section_content:
            sections.append((current_title, section_content))

    return sections


def main() -> int:
    strict_fetch = os.environ.get("STRICT_FETCH", "0") == "1"

    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    sources = load_sources(CONFIG_PATH)
    existing_manifest = load_existing_manifest(MANIFEST_PATH)
    existing_files = existing_manifest.get("files", {})

    new_files: Dict[str, Dict] = {}
    fetched_paths: Set[Path] = set()

    fetch_started_at = now_iso()
    total_sections = 0
    successful_sections = 0
    failed_sources: List[tuple[str, str]] = []

    for source in sources:
        print(f"[INFO] Source={source.source_id} url={source.llms_txt}")

        try:
            content = fetch_text(source.llms_txt)
            print(f"[INFO] Source={source.source_id} fetched {len(content)} bytes")

            # Extract sections from all-in-one content
            sections = extract_sections(content)
            print(f"[INFO] Source={source.source_id} discovered {len(sections)} sections")

            total_sections += len(sections)

            source_root = DOCS_ROOT / source.output_subdir
            source_root.mkdir(parents=True, exist_ok=True)

            for title, section_content in sections:
                try:
                    # Clean title for display
                    clean_title_str = clean_title(title)
                    # Generate unique filename with collision handling
                    base_filename = sanitize_filename(title)
                    filename = base_filename
                    counter = 1
                    while f"{source.output_subdir}/{filename}.md" in new_files:
                        counter += 1
                        filename = f"{base_filename}-{counter}"
                    
                    dest = source_root / f"{filename}.md"

                    digest = sha256_text(section_content)

                    existing = existing_files.get(f"{source.output_subdir}/{filename}.md", {})
                    existing_digest = existing.get("sha256")

                    if existing_digest != digest or not dest.exists():
                        dest.write_text(section_content, encoding="utf-8")

                    manifest_key = f"{source.output_subdir}/{filename}.md"
                    new_files[manifest_key] = {
                        "source": source.source_id,
                        "title": clean_title_str,
                        "sha256": digest,
                        "bytes": len(section_content.encode("utf-8")),
                        "fetched_at": fetch_started_at,
                    }
                    fetched_paths.add(dest)
                    successful_sections += 1
                    print(f"[OK] {manifest_key} ({clean_title_str})")

                except Exception as exc:
                    print(f"[WARN] failed section title={title} err={exc}")

        except Exception as exc:
            print(f"[ERROR] failed source={source.source_id} err={exc}")
            failed_sources.append((source.source_id, str(exc)))

    # Remove files that no longer exist
    previous_paths = set(existing_files.keys())
    current_paths = set(new_files.keys())
    removed_paths = sorted(previous_paths - current_paths)

    for removed in removed_paths:
        file_path = DOCS_ROOT / removed
        if file_path.exists():
            file_path.unlink()
            # Clean empty parent dirs
            parent = file_path.parent
            while parent != DOCS_ROOT and parent.exists():
                if any(parent.iterdir()):
                    break
                parent.rmdir()
                parent = parent.parent

    manifest = {
        "generated_at": now_iso(),
        "tool": "scripts/fetch_gemini_docs.py",
        "strict_fetch": strict_fetch,
        "sources": [
            {
                "id": s.source_id,
                "llms_txt": s.llms_txt,
                "output_subdir": s.output_subdir,
            }
            for s in sources
        ],
        "stats": {
            "total_sections": total_sections,
            "successful_sections": successful_sections,
            "failed_sources": len(failed_sources),
            "removed_files": len(removed_paths),
        },
        "failed": [{"source": src, "error": err} for src, err in failed_sources],
        "files": {k: new_files[k] for k in sorted(new_files.keys())},
    }

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print("\n[SUMMARY]")
    print(f"total_sections={total_sections}")
    print(f"successful_sections={successful_sections}")
    print(f"failed_sources={len(failed_sources)}")
    print(f"removed_files={len(removed_paths)}")

    if failed_sources and strict_fetch:
        print("[ERROR] STRICT_FETCH=1 and failures detected")
        return 1

    if successful_sections == 0:
        print("[ERROR] No documents fetched successfully")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
