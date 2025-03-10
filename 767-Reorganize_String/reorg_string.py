import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_hash = Counter(
            s
        )  # hashmap collection import {'blue': 3, 'red': 2, 'green': 1}
        # [('a', 2), ('b', 3), ('c', 1)] is what dict get converted to using .items
        maxHeap = [[-cnt, char] for char, cnt in char_hash.items()]
        heapq.heapify(maxHeap)  # O(n)
        out = ""
        # Save prev char so we dont reuse
        prev_char = None
        while maxHeap or prev_char:
            if not maxHeap and prev_char:
                return ""
            count, char = heapq.heappop(maxHeap)
            count += 1

            if prev_char:
                heapq.heappush(maxHeap, prev_char)
                prev_char = None

            if count != 0:
                prev_char = [count, char]

            out += char

        return out
