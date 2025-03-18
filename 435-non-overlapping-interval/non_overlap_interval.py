# Greedy by start time
# NOTE: intuition: if the a start time is before the previous end time then u
# remove the one that ends first
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        # check with prev
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res


# O(nlogn)
# O(n) or O(1) depending on sorting algo
