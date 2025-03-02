# 2 pointers: sorted start/end pts and compare
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        ptr_start, ptr_end = 0, 0
        out, count = 0, 0
        while ptr_end < len(intervals) and ptr_start < len(intervals):
            if start[ptr_start] < end[ptr_end]:
                count += 1
                ptr_start += 1
            else:
                # NOTE: If the value is equal it doesnt count as +1 we subtract first so that it doesnt go over the max,
                # and then we add it back anyways so no dif
                count -= 1
                ptr_end += 1

            out = max(out, count)

        return out
