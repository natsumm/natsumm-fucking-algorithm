"""Create a consistent directory for a new algorithm problem."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def valid_dir_name(value: str) -> str:
    if not value or "/" in value or "\\" in value or value in {".", ".."}:
        raise argparse.ArgumentTypeError("目录名不能为空，且不能包含路径分隔符")
    return value


def create_problem(number: str, title: str) -> Path:
    valid_dir_name(number)
    valid_dir_name(title)
    dir_name = f"{number}_{title}" if number != "-" else title
    target = ROOT / "practice" / dir_name
    if target.exists():
        raise FileExistsError(f"题目目录已存在：{target}")

    target.mkdir(parents=True)
    solution_template = (ROOT / "templates" / "leetcode_solution.py").read_text(encoding="utf-8")
    test_template = (ROOT / "templates" / "test_solution.py").read_text(encoding="utf-8")
    header = f"{title}（LeetCode {number}）" if number != "-" else title
    (target / "solution.py").write_text(
        solution_template.replace("题目名称（题号）", header, 1).replace(
            "practice/<题目目录名>", f"practice/{dir_name}", 1
        ),
        encoding="utf-8",
    )
    (target / "test_solution.py").write_text(
        test_template.replace("题目名称", title, 1)
        .replace("practice.<题目目录名>", f"practice.{dir_name}", 1),
        encoding="utf-8",
    )
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="创建一道算法练习题目录")
    parser.add_argument("number", help="题目编号；无编号的题传 -")
    parser.add_argument("title", help="中文题名，目录名形如 <编号>_<题名>")
    args = parser.parse_args()

    try:
        target = create_problem(args.number, args.title)
    except FileExistsError as error:
        parser.error(str(error))
    print(f"已创建：{target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
