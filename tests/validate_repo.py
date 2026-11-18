#!/usr/bin/env python3
"""Structural validation for the intelligent-business-analyst skill.

Standard library only (Python 3.9+). Checks:
  1. Required files exist (skill files under skills/intelligent-business-analyst/).
  2. SKILL.md frontmatter is present and valid for Agent Skills conventions.
  3. Every relative Markdown link resolves.
  4. Every reference file is linked from SKILL.md (progressive disclosure is wired).
  5. SKILL.md stays concise.
  6. Test cases contain the required sections.
  7. No obvious secrets or real-looking personal data.
  8. The skill folder carries no install/download instructions (keeps README-style setup paths
     out of what skill scanners and agents load; see Snyk W012).

It does NOT evaluate the skill's behaviour with a model; see tests/test-cases.md for that.

Usage: python3 tests/validate_repo.py [repo_root]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
SKILL_NAME = "intelligent-business-analyst"
SKILL_REL = f"skills/{SKILL_NAME}"
SKILL_DIR = ROOT / SKILL_REL

SKILL_FILES = [
    "SKILL.md", "LICENSE", "agents/openai.yaml",
    "references/requirement-engineering.md", "references/user-story-generator.md",
    "references/business-process-modeling.md", "references/business-rules-analyzer.md",
    "references/gap-analysis.md", "references/impact-analysis.md",
    "references/documentation-generator.md", "references/requirement-quality-review.md",
    "references/quality-scoring-rubric.md",
    "templates/brd-template.md", "templates/frd-template.md", "templates/user-story-template.md",
    "templates/business-rules-template.md", "templates/gap-analysis-template.md",
    "templates/impact-analysis-template.md", "templates/use-case-template.md",
    "templates/traceability-matrix-template.md",
]
REQUIRED = [f"{SKILL_REL}/{f}" for f in SKILL_FILES] + [
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", ".gitignore",
    "examples/ecommerce/README.md", "examples/insurance-api/README.md", "examples/ai-product/README.md",
    "tests/test-cases.md", "tests/evaluation-rubric.md", "tests/expected-outputs/README.md",
]

SKILL_MAX_LINES = 500
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.S)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_ALLOW = re.compile(r"@(example\.(com|org|net)|anthropic\.com)$|^noreply@", re.I)
SECRET_PATTERNS = {
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    "OpenAI/Anthropic-style key": re.compile(r"sk-(ant-)?[A-Za-z0-9_-]{20,}"),
    "Slack token": re.compile(r"xox[abprs]-[A-Za-z0-9-]{10,}"),
}
INSTALL_RE = re.compile(r"git clone|npx skills|pip install|curl |wget |https?://github\.com/[^\s)]+\.git", re.I)
# Only the frontmatter metadata.repository URL is allowed in the skill folder.
INSTALL_ALLOW = re.compile(r"^\s*repository:")
TEST_SECTIONS = ["**Input**", "**Expected behaviour:**", "**Expected artifacts:**",
                 "**Acceptance criteria:**", "**Failure conditions:**"]

errors: list[str] = []
warnings: list[str] = []


def check_required() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with '---' frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("frontmatter is not closed")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue  # nested keys (metadata) or comments
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_frontmatter() -> None:
    path = SKILL_DIR / "SKILL.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        return
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"frontmatter name invalid: {name!r}")
    if name != SKILL_NAME:
        errors.append(f"frontmatter name must be {SKILL_NAME!r} (it must match the skill folder)")
    if not desc:
        errors.append("frontmatter description missing")
    elif len(desc) > 1024:
        errors.append(f"frontmatter description too long ({len(desc)} > 1024)")
    if "<" in desc or ">" in desc:
        errors.append("frontmatter description must not contain angle brackets")
    unknown = set(fm) - {"name", "description", "license", "metadata", "allowed-tools", "compatibility"}
    if unknown:
        warnings.append(f"non-standard frontmatter keys: {sorted(unknown)}")
    lines = text.count("\n") + 1
    if lines > SKILL_MAX_LINES:
        errors.append(f"SKILL.md has {lines} lines (> {SKILL_MAX_LINES}); move content to references/")


def check_links() -> None:
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        body = FENCE_RE.sub("", md.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(body):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0]
            if not (md.parent / target_path).resolve().exists():
                errors.append(f"broken link in {md.relative_to(ROOT)}: {target}")


def check_progressive_disclosure() -> None:
    skill = SKILL_DIR / "SKILL.md"
    if not skill.is_file():
        return
    text = skill.read_text(encoding="utf-8")
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        if f"references/{ref.name}" not in text and f"references/{ref.stem})" not in text:
            errors.append(f"reference not linked from SKILL.md: references/{ref.name}")


def check_skill_folder() -> None:
    if not SKILL_DIR.is_dir():
        errors.append(f"skill folder missing: {SKILL_REL}/")
        return
    stray = [n for n in ("SKILL.md", "references", "templates", "agents") if (ROOT / n).exists()]
    if stray:
        errors.append(f"skill files must live in {SKILL_REL}/, found at repo root: {stray}")
    for f in sorted(SKILL_DIR.rglob("*")):
        if not f.is_file():
            continue
        if f.name.lower().startswith("readme"):
            errors.append(f"README inside the skill folder: {f.relative_to(ROOT)}")
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if INSTALL_RE.search(line) and not INSTALL_ALLOW.search(line):
                errors.append(f"install/download instruction in skill folder: {f.relative_to(ROOT)}:{n}")


def check_test_cases() -> None:
    path = ROOT / "tests" / "test-cases.md"
    if not path.is_file():
        return
    blocks = re.split(r"^## (TC-\d+)", path.read_text(encoding="utf-8"), flags=re.M)
    cases = dict(zip(blocks[1::2], blocks[2::2]))
    if len(cases) < 12:
        errors.append(f"expected at least 12 test cases, found {len(cases)}")
    for case_id, body in cases.items():
        for section in TEST_SECTIONS:
            if section not in body:
                errors.append(f"{case_id} missing section {section}")


def check_sensitive_data() -> None:
    for f in sorted(ROOT.rglob("*")):
        if not f.is_file() or ".git" in f.parts or f.suffix not in {".md", ".yaml", ".yml", ".py", ".txt"}:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for label, rx in SECRET_PATTERNS.items():
            if rx.search(text):
                errors.append(f"possible {label} in {f.relative_to(ROOT)}")
        for email in EMAIL_RE.findall(text):
            if not EMAIL_ALLOW.search(email):
                errors.append(f"email address found in {f.relative_to(ROOT)}: {email}")


def main() -> int:
    check_required()
    check_frontmatter()
    check_links()
    check_progressive_disclosure()
    check_skill_folder()
    check_test_cases()
    check_sensitive_data()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} error(s).")
        return 1
    print("OK  structure, frontmatter, links, references, skill folder, test cases and sensitive-data checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
