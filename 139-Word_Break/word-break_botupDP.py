from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # Base case: we start from back of string
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            # go thru every word in wordDict
            for w in wordDict:
                # Compare a) if enough char to compare, if yes compare it
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # word matchs so lets check the whole word (or up until now)
                    dp[i] = dp[i + len(w)]
                # if true we found a match we can go next index
                if dp[i]:
                    break
        # since its based on the prev match and the match before that etc.etc.
        return dp[0]


# NOTE::
# Time: O(n*m*t) (remember t w/ substring comparison)
# Space: O(n)
# Where n is the length of the string s,
# m is the number of words in wordDict
# t is the maximum length of any word in wordDict.
