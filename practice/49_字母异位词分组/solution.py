"""字母异位词分组（LeetCode 49）

- 来源：LeetCode 49
- 难度：中等（基础题）
- 核心标签：哈希表、字符串、排序
- 首次练习日期：2026-08-26
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/49_字母异位词分组/solution.py

题意摘要：
给定一个只包含小写字母的字符串数组，把互为字母异位词的字符串放进同一组。字母异位词使用相同的字母，并且每个字母出现的次数相同，只是排列顺序可能不同。分组和组内元素均可按任意顺序返回。

输入与输出：
- 输入：一个 JSON 字符串数组，例如 `["eat", "tea", "tan", "ate", "nat", "bat"]`。
- 输出：分组后的 JSON 二维字符串数组。
- 约束：`1 <= strs.length <= 10^4`，`0 <= strs[i].length <= 100`，字符串只包含小写字母。

解题思路：
互为字母异位词的字符串排序后一定相同。因此，遍历数组，把每个字符串排序后的结果作为哈希表的键，把原字符串追加到对应列表中，最后返回哈希表中的所有分组。

例如，`"eat"`、`"tea"` 和 `"ate"` 排序后都是 `"aet"`，所以会进入同一组。

复杂度：
设字符串数量为 `n`，每个字符串的最大长度为 `k`：
- 时间：`O(n * k log k)`，主要开销是逐个排序字符串。
- 空间：`O(n * k)`，用于保存分组及排序产生的键。

测试设计：
- 普通情况：包含三个不同分组。
- 空字符串：`[""]`。
- 单个字符：`["a"]`。
- 重复字符串和互为异位词的字符串同时出现。

复盘：
- 首次耗时：未记录
- 完成情况：独立完成
- 错误原因：无
- 学到的模式：当题目要求按“等价关系”分组时，可以寻找每组共有的规范化表示，并将它作为哈希表的键。
- 二刷日期与结果：待复习
"""

from __future__ import annotations

import json


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """按照字母异位关系对字符串进行分组。"""
    result: dict[str, list[str]] = {}
    for string in strs:
        key = "".join(sorted(string))
        if key not in result:
            result[key] = []
        result[key].append(string)
    return list(result.values())


def solve(data: str) -> str:
    """解析 JSON 字符串数组，并返回 JSON 格式的分组结果。"""
    strs = json.loads(data)
    return json.dumps(group_anagrams(strs), ensure_ascii=False)


def main() -> None:
    data1 = '["eat", "tea", "tan", "ate", "nat", "bat"]'
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    print(f"预期：{expected1}，实际：{group_anagrams(json.loads(data1))}")

    data2 = '[""]'
    expected2 = [[""]]
    print(f"预期：{expected2}，实际：{group_anagrams(json.loads(data2))}")

    data3 = '["a"]'
    expected3 = [["a"]]
    print(f"预期：{expected3}，实际：{group_anagrams(json.loads(data3))}")


if __name__ == "__main__":
    main()
