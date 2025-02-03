from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in index_map:
                return [index_map[diff], i]
            index_map[j] = i
