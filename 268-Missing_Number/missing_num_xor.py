from typing import List


# NOTE: XOR i^i = 0 any xor of same val = 0 cause u know, xor
# 101
# 101
# ----xorr
# 000
# now we just xor everything outa the i and the nums[i] the only one not xor'ed is the answer
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = n = len(nums)
        for i in range(n):
            xor ^= i ^ nums[i]
        return xor


# NOTE:
# O(n)
# O(1)
