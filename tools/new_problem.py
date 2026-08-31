"""Create a consistent directory for a new algorithm problem."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVELS = {
    1: "level_01_basics",
    2: "level_02_simulation",
    3: "level_03_two_pointers",
    4: "level_04_data_structures",
    5: "level_05_search",
    6: "level_06_dp_greedy",
    7: "level_07_graph_tree",
}


def valid_slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", value):
        raise argparse.ArgumentTypeError("slug 只能包含小写字母、数字和下划线")
    return value


def create_problem(level: int, slug: str, title: str) -> Path:
    target = ROOT / "practice" / LEVELS[level] / slug
    if target.exists():
        raise FileExistsError(f"题目目录已存在：{target}")

    target.mkdir(parents=True)
    problem_template = (ROOT / "templates" / "leetcode_problem.md").read_text(encoding="utf-8")
    solution_template = (ROOT / "templates" / "leetcode_solution.py").read_text(encoding="utf-8")
    test_template = (ROOT / "templates" / "test_solution.py").read_text(encoding="utf-8")
    (target / "README.md").write_text(
        problem_template.replace("# 题目名称", f"# {title}", 1), encoding="utf-8"
    )
    (target / "solution.py").write_text(
        solution_template.replace("题目名称", title, 1), encoding="utf-8"
    )
    (target / "test_solution.py").write_text(
        test_template.replace("题目名称", title, 1)
        .replace("__LEVEL_DIR__", LEVELS[level], 1)
        .replace("__SLUG__", slug, 1),
        encoding="utf-8",
    )
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="创建一道算法练习题目录")
    parser.add_argument("level", type=int, choices=LEVELS, help="学习等级 1-7")
    parser.add_argument("slug", type=valid_slug, help="英文目录名，如 attendance")
    parser.add_argument("title", help="题目显示名称")
    args = parser.parse_args()

    try:
        target = create_problem(args.level, args.slug, args.title)
    except FileExistsError as error:
        parser.error(str(error))
    print(f"已创建：{target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
