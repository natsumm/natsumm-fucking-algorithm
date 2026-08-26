"""最长连续序列：直接运行本文件即可查看测试结果。"""

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
