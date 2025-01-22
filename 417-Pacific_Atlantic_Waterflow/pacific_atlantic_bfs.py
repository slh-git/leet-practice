# We go from the the 2 atlantic vs 2 pacific edges. The edges we dfs to its own ocean.
# if we can reach the same cell from both pacific and atlantic, then we add it to the result.
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, atl = set(), set()
