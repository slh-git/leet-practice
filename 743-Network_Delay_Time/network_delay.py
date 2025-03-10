# NOTE: dijstra, minheap push pop, push neighbor etc
# adj list
# edgecase = u cant reach a node
from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        # make adjacency list
        for source, target, time in times:
            edges[source].append([target, time])

        minHeap = [(0, k)]
        visited = set()
        out = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            # if it pops is always gonna be larger (diff in vid)
            out = time
            for neighbor, ntime in edges[node]:
                # why? well cause its a min heap if u popped its already
                if neighbor not in visited:
                    # NOTE: to add time to keep track of total sum
                    heapq.heappush(minHeap, (time + ntime, neighbor))
        return out if len(visited) == n else -1


# NOTE: recall heap operations are log
# so the amount of times we push is roughly E*logE
