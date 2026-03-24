#!/usr/bin/env python3

from __future__ import annotations

import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "docs/src/main/asciidoc"
DEST_ROOT = REPO_ROOT / "docs/src/main/markdown"

TITLE_PATTERN = re.compile(r"^=+\s+(?P<title>.+?)\s*$", re.MULTILINE)
DESCRIPTION_PATTERN = re.compile(r"^:description:\s*(?P<description>.+?)\s*$", re.MULTILINE)
MARKDOWN_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)$")
FORMALPARA_PATTERN = re.compile(
    r'<div class="formalpara">\s*<div class="title">\s*(?P<title>.*?)\s*</div>\s*(?P<body>.*?)\s*</div>',
    re.DOTALL,
)
ABSOLUTE_DOC_PATH_PATTERN = re.compile(
    rf"(?P<path>{re.escape(str(SRC_ROOT.resolve()))}/[^)\]\"'\s<>]+?)(?P<fragment>#[^)\]\"'\s<>]+)?"
)
INLINE_LINK_PATTERN = re.compile(r"(?<!!)\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")
IMAGE_PATTERN = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<target>[^)]+)\)")
TARGET_SUFFIX_PATTERN = re.compile(
    r"\((?P<target>(?![a-z][a-z0-9+.-]*:)(?!/)[^()\[\]\s]+?\.(?:xml|adoc|html))(?P<fragment>#[^)]+)?\)",
    re.IGNORECASE,
)

ACRONYMS = {
    "adoc": "AsciiDoc",
    "ai": "AI",
    "api": "API",
    "apis": "APIs",
    "aws": "AWS",
    "cdi": "CDI",
    "cli": "CLI",
    "config": "Config",
    "cors": "CORS",
    "db": "DB",
    "dbclient": "DBClient",
    "faq": "FAQ",
    "graphql": "GraphQL",
    "grpc": "gRPC",
    "h1": "H1",
    "h2": "H2",
    "hcv": "HCV",
    "http": "HTTP",
    "https": "HTTPS",
    "idcs": "IDCS",
    "jdk": "JDK",
    "jep": "JEP",
    "jib": "Jib",
    "jms": "JMS",
    "json": "JSON",
    "jsonb": "JSON-B",
    "jsonp": "JSON-P",
    "jsonrpc": "JSON-RPC",
    "jwt": "JWT",
    "jpa": "JPA",
    "jaxrs": "JAX-RS",
    "k8s": "K8s",
    "kafka": "Kafka",
    "langchain4j": "LangChain4j",
    "lc4j": "LC4J",
    "lra": "LRA",
    "maven": "Maven",
    "md": "Markdown",
    "mcp": "MCP",
    "micrometer": "Micrometer",
    "mp": "MP",
    "neo4j": "Neo4j",
    "oci": "OCI",
    "oidc": "OIDC",
    "oke": "OKE",
    "openapi": "OpenAPI",
    "opentelemetry": "OpenTelemetry",
    "pem": "PEM",
    "pkcs": "PKCS",
    "pr": "PR",
    "quickstart": "Quick Start",
    "rag": "RAG",
    "readme": "README",
    "restclient": "REST Client",
    "rsoperators": "Reactive Streams Operators",
    "se": "SE",
    "sse": "SSE",
    "tls": "TLS",
    "ucp": "UCP",
    "uri": "URI",
    "urls": "URLs",
    "webclient": "WebClient",
    "webserver": "WebServer",
    "weblogic": "WebLogic",
    "websocket": "WebSocket",
    "xml": "XML",
    "yaml": "YAML",
}


@dataclass
class DocMetadata:
    title: str
    description: str


def run_command(args: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
        raise RuntimeError(f"command failed: {' '.join(args)}")
    return result.stdout


def derive_title(path: Path) -> str:
    words = re.split(r"[-_]+", path.stem)
    title_words = []
    for word in words:
        normalized = ACRONYMS.get(word.lower())
        if normalized:
            title_words.append(normalized)
        elif word:
            title_words.append(word.capitalize())
    return " ".join(title_words) or path.stem


def extract_title(source_text: str, source_path: Path) -> str:
    match = TITLE_PATTERN.search(source_text)
    if match:
        return match.group("title").strip()
    return derive_title(source_path)


def extract_description(source_text: str) -> str | None:
    match = DESCRIPTION_PATTERN.search(source_text)
    if match:
        return normalize_whitespace(match.group("description"))
    return None


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def convert_with_backend(source_path: Path, backend: str, pandoc_format: str, suffix: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
        temp_path = Path(temp_file.name)
    try:
        run_command(
            [
                "asciidoctor",
                "-S",
                "unsafe",
                "-a",
                "reproducible",
                "-b",
                backend,
                "-o",
                str(temp_path),
                str(source_path),
            ],
            cwd=REPO_ROOT,
        )
        return run_command(
            [
                "pandoc",
                "-f",
                pandoc_format,
                "-t",
                "gfm",
                "--wrap=none",
                str(temp_path),
            ],
            cwd=REPO_ROOT,
        )
    finally:
        temp_path.unlink(missing_ok=True)


def convert_adoc_to_markdown(source_path: Path) -> str:
    try:
        return convert_with_backend(source_path, "docbook", "docbook", ".xml")
    except RuntimeError:
        return convert_with_backend(source_path, "html5", "html-native_divs-native_spans", ".html")


def cleanup_formal_paragraphs(markdown: str) -> str:
    def replace(match: re.Match[str]) -> str:
        title = normalize_whitespace(match.group("title"))
        body = match.group("body").strip()
        return f"*{title}*\n\n{body}"

    return FORMALPARA_PATTERN.sub(replace, markdown)


def map_source_path_to_dest(raw_path: str, fragment: str | None, current_dest: Path) -> str:
    source_path = Path(raw_path)
    try:
        relative = source_path.relative_to(SRC_ROOT)
    except ValueError:
        return f"{raw_path}{fragment or ''}"

    if relative.suffix in {".adoc", ".xml"}:
        target = DEST_ROOT / relative.with_suffix(".md")
    else:
        target = DEST_ROOT / relative

    resolved = os.path.relpath(target, current_dest.parent).replace(os.sep, "/")
    return f"{resolved}{fragment or ''}"


def rewrite_absolute_paths(markdown: str, current_dest: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        return map_source_path_to_dest(match.group("path"), match.group("fragment"), current_dest)

    return ABSOLUTE_DOC_PATH_PATTERN.sub(replace, markdown)


def rewrite_relative_doc_links(markdown: str, current_dest: Path) -> str:
    def replace_target(target: str) -> str:
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return target
        if "{" in target or "%7B" in target or target.startswith("++https://"):
            return target

        fragment = ""
        if "#" in target:
            target, fragment = target.split("#", 1)
            fragment = f"#{fragment}"

        target_path = Path(target)

        if target.endswith((".xml", ".adoc", ".html")):
            normalized = target_path.with_suffix(".md").as_posix()
            return f"{posixpath.normpath(normalized)}{fragment}"

        if not target_path.suffix and target_path.name not in {"", "."}:
            candidate = (current_dest.parent / target_path).resolve()
            if candidate.with_suffix(".md").exists():
                normalized = target_path.with_suffix(".md").as_posix()
                return f"{posixpath.normpath(normalized)}{fragment}"
            try:
                candidate_rel = candidate.relative_to(DEST_ROOT.resolve())
            except ValueError:
                candidate_rel = None
            if candidate_rel and (SRC_ROOT / candidate_rel).with_suffix(".adoc").exists():
                normalized = target_path.with_suffix(".md").as_posix()
                return f"{posixpath.normpath(normalized)}{fragment}"

        return f"{target}{fragment}"

    def replace_links(match: re.Match[str]) -> str:
        label = match.group("label")
        target = replace_target(match.group("target"))
        return f"[{label}]({target})"

    def replace_images(match: re.Match[str]) -> str:
        alt = match.group("alt")
        target = replace_target(match.group("target"))
        return f"![{alt}]({target})"

    markdown = INLINE_LINK_PATTERN.sub(replace_links, markdown)
    return IMAGE_PATTERN.sub(replace_images, markdown)


def rewrite_target_suffixes(markdown: str) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        fragment = match.group("fragment") or ""
        if target.startswith(("http://", "https://", "mailto:", "/")):
            return match.group(0)
        return f"({Path(target).with_suffix('.md').as_posix()}{fragment})"

    return TARGET_SUFFIX_PATTERN.sub(replace, markdown)


def enforce_single_h1(markdown: str, title: str) -> str:
    markdown = markdown.lstrip()
    lines = markdown.splitlines()
    if lines and lines[0].strip() == f"# {title}":
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    adjusted_lines = []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            adjusted_lines.append(line)
            continue

        if not in_fence:
            heading = MARKDOWN_HEADING_PATTERN.match(line)
            if heading:
                hashes, text = heading.groups()
                adjusted_lines.append(f"{'#' * min(len(hashes) + 1, 6)} {text}")
                continue

        adjusted_lines.append(line)

    body = "\n".join(adjusted_lines).strip()
    if body:
        return f"# {title}\n\n{body}\n"
    return f"# {title}\n"


def cleanup_spacing(markdown: str) -> str:
    markdown = markdown.replace("\r\n", "\n")
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def summarize_markdown(markdown: str) -> str:
    in_fence = False
    paragraphs: list[str] = []
    current: list[str] = []

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if raw_line.startswith("```"):
            in_fence = not in_fence
            if current:
                paragraphs.append(normalize_whitespace(" ".join(current)))
                current = []
            continue
        if in_fence:
            continue
        if not line:
            if current:
                paragraphs.append(normalize_whitespace(" ".join(current)))
                current = []
            continue
        if line.startswith(("#", ">", "|", "-", "*")):
            if current:
                paragraphs.append(normalize_whitespace(" ".join(current)))
                current = []
            continue
        if line.startswith("<"):
            continue
        current.append(line)

    if current:
        paragraphs.append(normalize_whitespace(" ".join(current)))

    for paragraph in paragraphs:
        if len(paragraph) >= 24:
            return paragraph.rstrip(".")
    return "Documentation for this topic"


def relative_link(from_dir: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_dir).replace(os.sep, "/")


def copy_assets() -> None:
    for path in SRC_ROOT.rglob("*"):
        if not path.is_file() or path.suffix == ".adoc":
            continue
        destination = DEST_ROOT / path.relative_to(SRC_ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate_readmes(metadata_by_path: dict[Path, DocMetadata]) -> dict[Path, DocMetadata]:
    readme_metadata: dict[Path, DocMetadata] = {}
    markdown_dirs: set[Path] = set()
    for path in metadata_by_path:
        current = path.parent
        while True:
            markdown_dirs.add(current)
            if current == DEST_ROOT:
                break
            current = current.parent

    for directory in sorted(markdown_dirs):
        rows: list[tuple[str, str, str]] = []
        for file_path in sorted(directory.glob("*.md")):
            if file_path.name in {"README.md", "index.md"}:
                continue
            metadata = metadata_by_path[file_path]
            rows.append((metadata.title, relative_link(directory, file_path), metadata.description))

        subdirs = sorted(child for child in directory.iterdir() if child.is_dir())
        for subdir in subdirs:
            readme_path = subdir / "README.md"
            if not any(candidate == readme_path or candidate.is_relative_to(subdir) for candidate in metadata_by_path):
                continue
            title = derive_title(subdir)
            description = f"Index of {title} documentation"
            rows.append((title, relative_link(directory, readme_path), description))

        if not rows:
            continue

        rows.sort(key=lambda item: item[0].casefold())
        title = "Helidon Documentation" if directory == DEST_ROOT else derive_title(directory)
        summary = (
            "Index of Helidon documentation topics"
            if directory == DEST_ROOT
            else f"Index of {title} documentation"
        )
        table_lines = [
            f"# {title}",
            "",
            summary + ".",
            "",
            "| Topic | Description |",
            "| --- | --- |",
        ]
        for topic, target, description in rows:
            escaped_description = description.replace("|", "\\|")
            table_lines.append(f"| [{topic}]({target}) | {escaped_description} |")
        table_lines.append("")

        readme_path = directory / "README.md"
        write_file(readme_path, "\n".join(table_lines))
        readme_metadata[readme_path] = DocMetadata(title=title, description=summary)

    return readme_metadata


def verify_links(markdown_paths: list[Path]) -> list[str]:
    errors: list[str] = []

    for markdown_path in markdown_paths:
        content = markdown_path.read_text(encoding="utf-8")
        for match in INLINE_LINK_PATTERN.finditer(content):
            target = match.group("target")
            if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            if "{" in target or "%7B" in target or target.startswith("++https://"):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (markdown_path.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(f"{markdown_path.relative_to(REPO_ROOT)} -> missing {target}")
        for match in IMAGE_PATTERN.finditer(content):
            target = match.group("target")
            if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            if "{" in target or "%7B" in target or target.startswith("++https://"):
                continue
            path_part = target.split("#", 1)[0]
            resolved = (markdown_path.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(f"{markdown_path.relative_to(REPO_ROOT)} -> missing {target}")

    return errors


def repair_local_links(markdown_paths: list[Path]) -> None:
    def repair_target(markdown_path: Path, target: str) -> str:
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return target
        if "{" in target or "%7B" in target or target.startswith("++https://"):
            return target

        path_part, _, fragment = target.partition("#")
        if not path_part:
            return target

        resolved = (markdown_path.parent / path_part).resolve()
        if resolved.exists():
            return target

        for levels in range(1, 4):
            candidate_target = posixpath.normpath("../" * levels + path_part)
            candidate_resolved = (markdown_path.parent / candidate_target).resolve()
            if candidate_resolved.exists():
                if fragment:
                    return f"{candidate_target}#{fragment}"
                return candidate_target

        return target

    for markdown_path in markdown_paths:
        content = markdown_path.read_text(encoding="utf-8")

        def replace_link(match: re.Match[str]) -> str:
            return f"[{match.group('label')}]({repair_target(markdown_path, match.group('target'))})"

        def replace_image(match: re.Match[str]) -> str:
            return f"![{match.group('alt')}]({repair_target(markdown_path, match.group('target'))})"

        updated = INLINE_LINK_PATTERN.sub(replace_link, content)
        updated = IMAGE_PATTERN.sub(replace_image, updated)
        if updated != content:
            write_file(markdown_path, updated)


def main() -> int:
    DEST_ROOT.mkdir(parents=True, exist_ok=True)
    copy_assets()

    metadata_by_path: dict[Path, DocMetadata] = {}
    adoc_files = sorted(SRC_ROOT.rglob("*.adoc"))

    for source_path in adoc_files:
        source_text = source_path.read_text(encoding="utf-8")
        title = extract_title(source_text, source_path)
        description = extract_description(source_text)
        destination = DEST_ROOT / source_path.relative_to(SRC_ROOT).with_suffix(".md")
        markdown = convert_adoc_to_markdown(source_path)
        markdown = cleanup_formal_paragraphs(markdown)
        markdown = rewrite_absolute_paths(markdown, destination)
        markdown = rewrite_relative_doc_links(markdown, destination)
        markdown = rewrite_target_suffixes(markdown)
        markdown = enforce_single_h1(markdown, title)
        markdown = cleanup_spacing(markdown)

        write_file(destination, markdown)
        metadata_by_path[destination] = DocMetadata(
            title=title,
            description=description or summarize_markdown(markdown),
        )

    metadata_by_path.update(generate_readmes(metadata_by_path))

    markdown_paths = sorted(DEST_ROOT.rglob("*.md"))
    repair_local_links(markdown_paths)
    link_errors = verify_links(markdown_paths)
    if link_errors:
        print("Broken links detected:", file=sys.stderr)
        for error in link_errors[:200]:
            print(error, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
