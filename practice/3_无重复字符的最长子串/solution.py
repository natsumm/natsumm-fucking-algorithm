"""无重复字符的最长子串：直接运行本文件即可查看测试结果。"""

from __future__ import annotations

import json


def length_of_longest_substring(s: str) -> int:
    """返回字符串中不含重复字符的最长子串长度。"""
    chars: set[str] = set()
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        while char in chars:
            chars.remove(s[left])
            left += 1

        chars.add(char)
        max_len = max(max_len, right - left + 1)

    return max_len


def solve(data: str) -> str:
    """解析 JSON 字符串，返回最长无重复字符子串的长度。"""
    s: str = json.loads(data)
    return str(length_of_longest_substring(s))


def main() -> None:
    data1 = '"abcabcbb"'
    expected1 = "3"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = '"bbbbb"'
    expected2 = "1"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = '"pwwkew"'
    expected3 = "3"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = '""'
    expected4 = "0"
    print(f"预期：{expected4}，实际：{solve(data4)}")

    data5 = '"a b a"'
    expected5 = "3"
    print(f"预期：{expected5}，实际：{solve(data5)}")


if __name__ == "__main__":
    main()
