"""最小覆盖子串（LeetCode 76）

- 来源：LeetCode
- 题号：76
- 英文名：Minimum Window Substring
- 难度：困难
- 核心标签：哈希表、字符串、滑动窗口
- 链接：https://leetcode.cn/problems/minimum-window-substring/
- 运行本题目测试：python3.12 -m pytest practice/76_最小覆盖子串

题目描述：
给定两个字符串 `s` 和 `t` ，长度分别是 `m` 和 `n` ，返回 `s` 中的 最短窗口 子串，使得该子串包含 `t` 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 `""`。

测试用例保证答案唯一。

输入与输出：
- 输入：字符串 `s`、字符串 `t`
- 输出：`s` 中包含 `t` 所有字符的最短子串；不存在则返回空字符串 `""`

示例 1：
- 输入：`s = "ADOBECODEBANC"`，`t = "ABC"`
- 输出：`"BANC"`
- 解释：最小覆盖子串 `"BANC"` 包含来自字符串 `t` 的 `'A'`、`'B'` 和 `'C'`。

示例 2：
- 输入：`s = "a"`，`t = "a"`
- 输出：`"a"`
- 解释：整个字符串 `s` 是最小覆盖子串。

示例 3：
- 输入：`s = "a"`，`t = "aa"`
- 输出：`""`
- 解释：`t` 中两个字符 `'a'` 均应包含在 `s` 的子串中，因此没有符合条件的子字符串，返回空字符串。

提示：
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` 和 `t` 由英文字母组成

官方示例与边界用例见同目录 `test_solution.py`。
"""

from __future__ import annotations


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        raise NotImplementedError("Solution 尚未实现")
