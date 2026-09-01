"""最长连续序列（LeetCode 128）

- 来源：LeetCode 128
- 难度：中等
- 核心标签：数组、哈希表、集合
- 首次练习日期：2026-08-26
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/128_最长连续序列/solution.py

题意摘要：
给定一个未排序的整数数组 `nums`，找出其中最长的数字连续序列，并返回该序列的长度。连续序列中的元素不要求在原数组中相邻，算法的时间复杂度要求为 `O(n)`。

输入与输出：
- 输入：一个 JSON 整数数组，例如 `[100, 4, 200, 1, 3, 2]`。
- 输出：最长连续序列的长度，例如 `4`。
- 约束：`0 <= nums.length <= 10^5`，`-10^9 <= nums[i] <= 10^9`。

解题思路：
先把所有数字放入集合：既可以去重，也可以在平均 `O(1)` 时间内判断某个数字是否存在。

遍历集合中的数字 `n`：

1. 如果 `n - 1` 也在集合中，说明 `n` 不是一段连续序列的起点，直接跳过。
2. 如果 `n - 1` 不在集合中，就从 `n` 开始不断检查 `n + 1`、`n + 2`……，统计这段连续序列的长度。
3. 用当前长度更新最大值。

例如集合中有 `{1, 2, 3, 4}`。只有 `1` 的前一个数字 `0` 不在集合中，因此只会从 `1` 向后完整扫描一次；`2`、`3`、`4` 都不会重复扫描后续序列。

两种实现：
- `solve()`：记录我的原答案。使用 `for offset in range(1, len(nums))` 从序列起点向后寻找数字，并在长度增加时更新最大值。
- `solve_by_gpt()`：记录 GPT 的参考答案。使用 `while current + 1 in nums_set` 向后扩展，完成一段序列后统一更新最大值。

两种实现采用相同的哈希集合思路，结果和平均时间复杂度相同。GPT 的写法不需要人为设置循环上界，表达上更贴近“只要下一个数字存在，就继续扩展”。

为什么是 O(n)：
虽然代码中有嵌套的 `while`，但只有连续序列的起点会进入循环。每个数字最多在遍历集合时被访问一次，并在所属序列向后扩展时再被检查一次，因此所有扩展操作的总次数是 `O(n)`，而不是 `O(n^2)`。

复杂度：
- 时间：平均 `O(n)`。
- 空间：`O(n)`，用于存储去重后的数字集合。

测试设计：
- 普通情况：`[100, 4, 200, 1, 3, 2]`，答案为 `4`。
- 含重复数字：`[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`，答案为 `9`。
- 重复值位于序列中：`[1, 0, 1, 2]`，答案为 `3`。
- 空数组：`[]`，答案为 `0`。
- 全是不连续数字：`[10, 30, 20]`，答案为 `1`。

复盘：
- 首次耗时：未记录
- 完成情况：独立完成
- 原答案评价：思路和结果都正确，也满足平均 `O(n)` 时间复杂度。使用 `range(1, len(nums))` 作为扩展上界是安全的，但这个上界与题意没有直接关系，`while` 更能清楚表达“下一个连续数字存在就继续”。
- 学到的模式：处理连续数字区间时，先用集合快速判断元素是否存在，再只从没有前驱的数字开始扩展，可以避免重复扫描。
- 二刷日期与结果：待复习
"""

from __future__ import annotations

import json


def solve(data: str) -> str:
    """使用我的答案求最长连续序列的长度。"""
    nums: list[int] = json.loads(data)
    if not nums:
        return "0"

    nums_set = set(nums)
    max_count = 1

    for number in nums_set:
        count = 1
        if number - 1 in nums_set:
            continue

        for offset in range(1, len(nums)):
            if number + offset not in nums_set:
                break
            count += 1
            if count > max_count:
                max_count = count

    return str(max_count)


def solve_by_gpt(data: str) -> str:
    """使用 GPT 的参考答案求最长连续序列的长度。"""
    nums: list[int] = json.loads(data)
    if not nums:
        return "0"

    nums_set = set(nums)
    max_count = 0

    for number in nums_set:
        if number - 1 in nums_set:
            continue

        current = number
        count = 1
        while current + 1 in nums_set:
            current += 1
            count += 1

        max_count = max(max_count, count)

    return str(max_count)


def main() -> None:
    data1 = "[100, 4, 200, 1, 3, 2]"
    print(f"预期：4，我的答案：{solve(data1)}，GPT 答案：{solve_by_gpt(data1)}")

    data2 = "[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]"
    print(f"预期：9，我的答案：{solve(data2)}，GPT 答案：{solve_by_gpt(data2)}")

    data3 = "[1, 0, 1, 2]"
    print(f"预期：3，我的答案：{solve(data3)}，GPT 答案：{solve_by_gpt(data3)}")

    data4 = "[]"
    print(f"预期：0，我的答案：{solve(data4)}，GPT 答案：{solve_by_gpt(data4)}")

    data5 = "[10, 30, 20]"
    print(f"预期：1，我的答案：{solve(data5)}，GPT 答案：{solve_by_gpt(data5)}")


if __name__ == "__main__":
    main()
