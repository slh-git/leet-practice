from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # gotta include the last cause py weird
        for i in range(n - 3, -1, -1):
            # so u go from back to front replacing inline
            # NOTE: reminder to +=
            cost[i] = min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
