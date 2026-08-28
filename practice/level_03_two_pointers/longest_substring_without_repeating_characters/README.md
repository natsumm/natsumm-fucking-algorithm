# 无重复字符的最长子串

- 来源：LeetCode 3
- 难度：中等
- 核心标签：字符串、哈希集合、滑动窗口
- 首次练习日期：2026-08-28
- 首次耗时：未记录

## 题目描述

给定一个字符串 `s`，找出其中不含重复字符的最长子串的长度。

注意：子串必须是原字符串中连续的一段，子序列则不要求连续。

## 示例

示例 1：

```text
输入：s = "abcabcbb"
输出：3
解释：无重复字符的最长子串可以是 "abc"、"bca" 或 "cab"。
```

示例 2：

```text
输入：s = "bbbbb"
输出：1
解释：无重复字符的最长子串是 "b"。
```

示例 3：

```text
输入：s = "pwwkew"
输出：3
解释：无重复字符的最长子串是 "wke"。"pwke" 是子序列，不是子串。
```

## 提示

- `0 <= s.length <= 10^5`
- `s` 由英文字母、数字、符号和空格组成

## 我的暴力思路

从每个位置开始向右枚举字符，遇到重复字符时停止，并记录得到的最大长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for left in range(len(s)):
            tmp = s[left]
            for right in range(left + 1, len(s)):
                if s[right] not in tmp:
                    tmp += s[right]
                else:
                    break
            max_len = max(max_len, len(tmp))

        return max_len
```

这个思路能够得到正确答案，但会重复检查许多已经遍历过的区间。字符串中的成员查询和拼接也不是常数时间，最坏情况下时间复杂度可达到 `O(n^3)`。

## 滑动窗口解法

维护窗口 `s[left:right + 1]`，并用集合 `chars` 保存窗口中的字符，保证窗口内始终没有重复字符。

当 `s[right]` 已经出现在集合中时，不断移除窗口最左侧的字符并移动 `left`，直到可以安全地加入当前字符。之后使用 `right - left + 1` 更新最长长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1

            chars.add(char)
            max_len = max(max_len, right - left + 1)

        return max_len
```

## 复杂度

- 时间复杂度：`O(n)`。每个字符最多被右指针加入集合一次，并被左指针移除一次。
- 空间复杂度：`O(min(n, |Σ|))`，其中 `|Σ|` 是字符集大小。

## 测试设计

- 普通重复：`"abcabcbb"` → `3`
- 全部相同：`"bbbbb"` → `1`
- 重复字符位于窗口中间：`"pwwkew"` → `3`
- 空字符串：`""` → `0`
- 包含空格：`"a b a"` → `3`

## 复盘

- 完成情况：先写出暴力解法，在提示下学习滑动窗口优化
- 学到的模式：求满足某种约束的最长连续子串时，可以尝试维护一个合法的滑动窗口
- 易错点：发现重复字符后要使用 `while` 持续收缩窗口，直到窗口重新合法
- 二刷日期与结果：待复习
