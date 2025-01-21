# We go from the the 2 atlantic vs 2 pacific edges. The edges we dfs to its own ocean. If we can reach the same cell from both pacific and atlantic, then we add it to the result.
# if we can reach the same cell from both pacific and atlantic, then we add it to the result.
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                ((r, c) in visit)
                or (r < 0)
                or (r >= Rows)
                or (c < 0)
                or (c >= Cols)
                or (heights[r][c] < prevHeight)
            ):
                # if visited, out of bound or height is lower than previous height (BECAUSE WE GOING FROM LOW TO HIGH)
                return
            visit.add((r, c))
            # add dfs to other neighbors 4 of them
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # find all the rows
        for c in range(Cols):
            dfs(0, c, pac, heights[0][c])
            dfs(Rows - 1, c, atl, heights[Rows - 1][c])

        # find all collumns
        for r in range(Rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Cols - 1, atl, heights[r][Cols - 1])

        out = []
        # find overlap
        for r in range(Rows):
            for c in range(Cols):
                if (r, c) in pac and (r, c) in atl:
                    out.append([r, c])

        return out
