# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

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
