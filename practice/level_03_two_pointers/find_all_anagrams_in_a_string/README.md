# 找到字符串中所有字母异位词

- 来源：[LeetCode 438](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
- 难度：中等
- 核心标签：哈希表、字符串、滑动窗口
- 首次练习日期：2026-08-31
- 首次耗时：未记录

## 题目描述

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的异位词子串，返回这些子串的起始索引。不考虑答案输出的顺序。

## 示例

示例 1：

```text
输入：s = "cbaebabacd", p = "abc"
输出：[0, 6]
解释：起始索引为 0 的子串 "cba" 和起始索引为 6 的子串 "bac" 都是 "abc" 的异位词。
```

示例 2：

```text
输入：s = "abab", p = "ab"
输出：[0, 1, 2]
解释：子串 "ab"、"ba"、"ab" 都是 "ab" 的异位词。
```

## 提示

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` 和 `p` 仅包含小写字母

## 解题思路

先统计 `p` 中每个字符的出现次数，再建立一个长度为 `len(p)` 的滑动窗口，并统计窗口中的字符频次。

每次比较窗口频次与 `p` 的频次：如果相同，就记录窗口左端点。窗口右移时，将离开窗口的字符计数减一，将新进入窗口的字符计数加一。计数降为零的字符要从字典中删除，确保两个频次字典可以直接比较。

## 代码

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        chars_dict = {}
        for w in p:
            chars_dict[w] = chars_dict.get(w, 0) + 1

        res = []
        window = {}
        left = 0
        right = left + len(p)

        for w in s[left:right]:
            window[w] = window.get(w, 0) + 1

        while right <= len(s):
            if window == chars_dict:
                res.append(left)
            if right == len(s):
                break

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            window[s[right]] = window.get(s[right], 0) + 1
            left += 1
            right += 1

        return res
```

## 复杂度

- 时间复杂度：`O(n)`。窗口在 `s` 上移动一次；字符集只有 26 个小写字母，字典比较可视为常数时间。
- 空间复杂度：`O(|Σ|)`，其中 `|Σ|` 为字符集大小，本题最多为 26。

## 测试设计

- 普通情况：`s = "cbaebabacd", p = "abc"` → `[0, 6]`
- 窗口连续重叠：`s = "abab", p = "ab"` → `[0, 1, 2]`
- 整个字符串就是异位词：`s = "baa", p = "aab"` → `[0]`
- `p` 比 `s` 长：`s = "a", p = "ab"` → `[]`

## 复盘

- 完成情况：已解答
- 学到的模式：固定长度的子串匹配问题可以使用固定窗口，并在移动时增量维护统计信息
- 易错点：字符计数变为零时要删除对应键，否则字典中残留的零计数会导致比较失败
- 二刷日期与结果：待复习
