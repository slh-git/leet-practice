from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = max(nums)

        for x in nums:
            temp = x * currMax
            currMax = max(x * currMax, x * currMin, x)
            currMin = min(temp, x * currMin, x)
            res = max(res, currMax)
        return res


# NOTE: O(n) O(1)
