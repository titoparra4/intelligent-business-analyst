# Contributing to Intelligent Business Analyst

Thanks for helping improve the skill. Priorities, in order:
**fidelity to the source > traceability > testability > clarity > brevity.**

## Ground rules

- **No fabricated content.** Examples must not present invented business rules, regulations or metrics
  as facts; unknown values are `TBD` with an open question.
- **Synthetic data only.** No real company, customer or personal data in examples or tests.
- **Progressive disclosure.** Keep `SKILL.md` short (the validator enforces < 500 lines). Specialized
  guidance goes in `references/`; reusable document skeletons go in `templates/`.
- **Stable ID scheme.** If you add an artifact type, add its prefix to the ID scheme in `SKILL.md`.
- **No mandatory dependencies.** The skill must work as plain Markdown instructions.
- **Honest claims.** Do not claim platform compatibility or test results you have not verified.

## Making a change

1. Edit the relevant reference/template. If behaviour changes, update or add a test case in
   `tests/test-cases.md` (Input, Expected behaviour, Expected artifacts, Acceptance criteria, Failure
   conditions) and, where useful, a reference output in `tests/expected-outputs/`.
2. If you change the scoring rubric, bump its version and re-check the worked example and the TC-10
   reference output arithmetic.
3. Run the structural validator:

   ```bash
   python3 tests/validate_repo.py
   ```

4. Optionally run affected behavioural cases in your agent and record real results in the results log.
5. Update `CHANGELOG.md` under `[Unreleased]`.

## Pull requests

Describe the behaviour change, the test cases affected and which platforms you tried it on (if any).
