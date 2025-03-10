from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i, a in enumerate(nums):
            # check if curr value is repeated
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            # NOTE: Do 2sum II (aka sorted 2pter)
            while l < r:
                threesum = a + nums[l] + nums[r]
                # if too big decrement right vice versa
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    out.append([a, nums[l], nums[r]])
                    # NOTE: we only have to check if left is incremented correctly cause the other 2 figures itself out by 2sum
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return out


# Time Complexity: O(n^2)
# The algorithm involves sorting the input array (O(n log n)) and then
# using a two-pointer approach inside a loop that runs O(n) times.
# This results in an overall complexity of O(n^2).

# Space Complexity:
# O(1) if sorting is done in place and only a constant amount of extra space is used.
# O(n) if additional space is required for storing the output or using an auxiliary data structure.
