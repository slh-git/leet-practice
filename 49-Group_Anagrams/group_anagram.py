from collections import defaultdict
from typing import List


# Count the letter combo of each word, using the count as a key insert it into a defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # noqa: F821
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += (
                    1  # Ascii # of letter - ascii of a to get the index
                )
            res[tuple(count)].append(s)  # tuple cause cant take list
        return list(res.values())
