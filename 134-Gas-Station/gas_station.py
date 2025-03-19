from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # index of best result
        out = 0
        totalSum = 0
        for i in range(len(gas)):
            totalSum += gas[i] - cost[i]
            if totalSum < 0:
                totalSum = 0
                out = i + 1
                continue

        return out
