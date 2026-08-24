"""考勤信息。

解题前先在同目录 README.md 中写清思路和复杂度。
"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
    """解析输入并返回最终输出文本。"""
    raise NotImplementedError("请实现 solve")


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        print(result)


if __name__ == "__main__":
    main()
