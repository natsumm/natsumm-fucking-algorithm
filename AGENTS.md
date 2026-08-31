# Project Instructions

## Python environment

- This project uses Python 3.12 on the current computer.
- Use `python3.12` for Python-related commands.
- Codex command subprocesses may not inherit the interactive terminal's `PATH`. If `python3.12` is unavailable there, use `./.venv/bin/python`, which is the project's verified Python 3.12 interpreter.
- Do not use the system `python` or `python3` commands for this project.
- Verify the selected interpreter reports Python 3.12 before diagnosing compatibility problems.
- Run scripts with `python3.12 path/to/script.py` (or the fallback interpreter above).
- Install packages with `python3.12 -m pip` (or the fallback interpreter above).
- Run tests with `python3.12 -m pytest` (or the fallback interpreter above).

## Algorithm problem structure (exercises you solve yourself)

The rules below describe the existing exercises created before the pytest workflow. New problems initialized by a coding agent follow the next section instead.

- Keep each algorithm exercise simple: normally use only `README.md` and `solution.py`.
- Put the algorithm and input parsing in `solve(data: str) -> str`.
- Do not read from `sys.stdin` in an exercise's `main()`.
- Write a small number of test-case input strings directly in `main()` and print both the expected and actual results.
- Test-case strings must follow the problem's real input format, including required newlines.
- Prefer clear, explicit cases over a generic test framework; do not add `TEST_CASES`, `check()`, terminal detection, or elaborate validation unless specifically needed.
- Do not create `sample_input.txt` or `sample_output.txt`; document the official sample in `README.md` or place it directly in `main()`.

## Coding Agent problem initialization

When the user asks a coding agent to initialize a new LeetCode problem, the agent creates exactly one new directory `practice/level_XX_topic/<slug>/` (reusing the existing level directories and snake_case slugs) with exactly three files, and changes nothing else.

Files to create:

- `README.md` — problem statement only: source, problem number, English name, difficulty, tags, link, the full original statement, input/output specification, constraints, and official examples.
- `solution.py` — LeetCode code template only: `from __future__ import annotations` plus a `class Solution` whose methods are the problem's method signature(s). Every method body is exactly `raise NotImplementedError("Solution 尚未实现")`.
- `test_solution.py` — pytest cases for the official examples and a few edge cases. Import the template by full module path (`from practice.<level_dir>.<slug>.solution import Solution`) and keep the module-level marker `pytestmark = pytest.mark.xfail(raises=NotImplementedError, reason="Solution 尚未实现")`.

Hard constraints while initializing:

- Do NOT implement any algorithm. Do NOT write pseudocode, hints, solution ideas, complexity analysis, or reference answers in any file, comment, or docstring.
- Do NOT modify existing files (README.md, roadmap.md, notes/, templates/, tools/, existing problems) and do NOT create files outside the new problem directory.
- Do NOT remove or weaken the xfail marker; the user removes it after implementing the solution.

Verification after initialization:

- Run `python3.12 -m pytest practice/<level_dir>/<slug>` for the single problem and `python3.12 -m pytest` for the full suite.
- Report results by category: collection/import errors (`ERROR`) are environment problems to fix; `xfailed` is expected because the solution is not implemented; `failed` means a real test failure.
