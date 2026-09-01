"""找到字符串中所有字母异位词（LeetCode 438）

- 来源：LeetCode 438，https://leetcode.cn/problems/find-all-anagrams-in-a-string/
- 难度：中等
- 核心标签：哈希表、字符串、滑动窗口
- 首次练习日期：2026-08-31
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/438_找到字符串中所有字母异位词/solution.py

题目描述：
给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的异位词子串，返回这些子串的起始索引。不考虑答案输出的顺序。

示例 1：
输入：s = "cbaebabacd", p = "abc"
输出：[0, 6]
解释：起始索引为 0 的子串 "cba" 和起始索引为 6 的子串 "bac" 都是 "abc" 的异位词。

示例 2：
输入：s = "abab", p = "ab"
输出：[0, 1, 2]
解释：子串 "ab"、"ba"、"ab" 都是 "ab" 的异位词。

提示：
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` 和 `p` 仅包含小写字母

解题思路：
先统计 `p` 中每个字符的出现次数，再建立一个长度为 `len(p)` 的滑动窗口，并统计窗口中的字符频次。

每次比较窗口频次与 `p` 的频次：如果相同，就记录窗口左端点。窗口右移时，将离开窗口的字符计数减一，将新进入窗口的字符计数加一。计数降为零的字符要从字典中删除，确保两个频次字典可以直接比较。

复杂度：
- 时间复杂度：`O(n)`。窗口在 `s` 上移动一次；字符集只有 26 个小写字母，字典比较可视为常数时间。
- 空间复杂度：`O(|Σ|)`，其中 `|Σ|` 为字符集大小，本题最多为 26。

测试设计：
- 普通情况：`s = "cbaebabacd", p = "abc"` → `[0, 6]`
- 窗口连续重叠：`s = "abab", p = "ab"` → `[0, 1, 2]`
- 整个字符串就是异位词：`s = "baa", p = "aab"` → `[0]`
- `p` 比 `s` 长：`s = "a", p = "ab"` → `[]`

复盘：
- 完成情况：已解答
- 学到的模式：固定长度的子串匹配问题可以使用固定窗口，并在移动时增量维护统计信息
- 易错点：字符计数变为零时要删除对应键，否则字典中残留的零计数会导致比较失败
- 二刷日期与结果：待复习
"""

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
