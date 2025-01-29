from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        check = [0] * (n + 1)
        # gotta include the last cause py weird
        for i in range(2, n + 1):
            # so what is teh best path to i ?
            check[i] = min(check[i - 1] + cost[i - 1], check[i - 2] + cost[i - 2])

        return check[n]
