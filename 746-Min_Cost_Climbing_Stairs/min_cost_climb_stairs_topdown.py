from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        check = [-1] * (n)

        def dfs(i):
            if i >= len(cost):
                return 0
            if check[i] != -1:
                return check[i]
            check[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return check[i]

        return min(dfs(0), dfs(1))
