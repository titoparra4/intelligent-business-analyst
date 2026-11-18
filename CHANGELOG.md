# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.1.0] - 2026-11-18

### Changed

- **Repository layout:** the installable skill moved from the repository root to
  `skills/intelligent-business-analyst/` (`SKILL.md`, `references/`, `templates/`, `agents/`, plus a
  copy of `LICENSE`). README, docs, examples and tests stay at the root and are no longer part of the
  installed skill. Motivation: skill scanners analyse the skill folder, and Snyk flagged the README's
  install instructions (W012, "unverifiable external dependency").
- **Breaking for manual installs:** cloning the repository directly into `~/.claude/skills/` no
  longer works; clone elsewhere and copy `skills/intelligent-business-analyst/` (see README §5).
  `npx skills add titoparra4/intelligent-business-analyst` keeps working.
- `tests/validate_repo.py` validates the new layout and fails if the skill folder contains a README,
  install commands or download URLs.
- User manuals (`docs/User-manual.pdf`, `docs/Manual-de-usuario.pdf`): cover version and the
  installation chapter updated for v1.1.0 and the new layout.

### Security

- README hardening related to Snyk W012 ("unverifiable external dependency"): pinned every install
  command (including `--list`) to the release tag, documented how to verify the release commit, and
  clarified that README URLs are install-time only.

## [1.0.0] - 2026-11-12

### Added

- `SKILL.md` entry point with module selection, workflow, ambiguity policy, ID scheme, output contract
  and safety rules.
- Eight module references: requirement engineering, user story generator, business process modeling,
  business rules analyzer, gap analysis, impact analysis, documentation generator and requirement
  quality review.
- Requirement Quality Score rubric (v1.0) with configurable weights, caps and bands.
- Eight Markdown templates (BRD, FRD/SRS, user stories, business rules, gap analysis, impact analysis,
  use case, traceability matrix).
- Three synthetic end-to-end examples: e-commerce coupons (Spanish), insurance policy API, AI support assistant.
- Twelve behavioural test cases, evaluation rubric, reference outputs and a structural validator
  (`tests/validate_repo.py`, standard library only).
- OpenAI Codex display metadata (`agents/openai.yaml`).
