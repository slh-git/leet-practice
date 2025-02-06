from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # NOTE: Python no maxheap so we just convert it to neg and use minheap ez
        stones = [-s for s in stones]

        # NOTE: O(n) time complexity
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            # if equal then its already removed
            if stone1 != stone2:
                # NOTE: stone 1 is smaller (because bigger number converted to negative) so no additional converting needed
                heapq.heappush(stones, stone1 - stone2)

        # NOTE: Edge case if there is no stone
        stones.append(0)

        # remember to convert it back to positive
        return abs(stones[0])
