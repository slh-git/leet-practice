from typing import List


# NOTE: add all n #s and add all nums, subtract and u get the missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out_sum = n = len(nums)
        for i in range(n):
            out_sum += i - nums[i]
        return out_sum


# NOTE:
# O(n)
# O(1)
