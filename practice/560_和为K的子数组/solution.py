"""和为 K 的子数组（LeetCode 560）。

LeetCode 代码模板：仅保留方法签名，不包含任何实现。
实现解法后运行 `python3.12 -m pytest` 验证，或自行补充 `main()` 直接运行本文件。
"""

from __future__ import annotations

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """统计并返回和为 k 的连续非空子数组的个数。"""
        prefix_count = {0:1}
        prefix_sum  = 0
