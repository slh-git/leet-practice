from typing import List
# NOTE: Equation is min(maxLeft, maxRight) - height[i]
# but if you pay attention the bounding side is always the lower side
# a slightly worse solution is to keep track of maxLeft and maxRight in separate arrays
# O(n) O(1) / O(n) O(n) for slightly worse


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # pointers
        l, r = 0, len(height) - 1
        # Keeping track of maxLeft value and max right value
        maxL, maxR = height[l], height[r]
        out = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                out += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                out += maxR - height[l]
        return out
