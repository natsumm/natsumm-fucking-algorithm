"""找到字符串中所有字母异位词：直接运行本文件即可查看测试结果。"""

from __future__ import annotations

import json


def find_anagrams(s: str, p: str) -> list[int]:
    """返回 s 中所有 p 的异位词子串的起始索引。"""
    chars_dict: dict[str, int] = {}
    for char in p:
        chars_dict[char] = chars_dict.get(char, 0) + 1

    result: list[int] = []
    window: dict[str, int] = {}
    left = 0
    right = len(p)

    for char in s[left:right]:
        window[char] = window.get(char, 0) + 1

    while right <= len(s):
        if window == chars_dict:
            result.append(left)
        if right == len(s):
            break

        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        window[s[right]] = window.get(s[right], 0) + 1
        left += 1
        right += 1

    return result


def solve(data: str) -> str:
    """解析包含 s 和 p 的 JSON 对象，返回 JSON 格式的起始索引。"""
    params: dict[str, str] = json.loads(data)
    return json.dumps(find_anagrams(params["s"], params["p"]), ensure_ascii=False)


def main() -> None:
    data1 = '{"s": "cbaebabacd", "p": "abc"}'
    expected1 = "[0, 6]"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = '{"s": "abab", "p": "ab"}'
    expected2 = "[0, 1, 2]"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = '{"s": "baa", "p": "aab"}'
    expected3 = "[0]"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = '{"s": "a", "p": "ab"}'
    expected4 = "[]"
    print(f"预期：{expected4}，实际：{solve(data4)}")


if __name__ == "__main__":
    main()
