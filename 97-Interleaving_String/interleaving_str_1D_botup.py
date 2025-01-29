# note: you see you can seperate to sub problems its probs dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)

        if len_s1 + len_s2 != len_s3:
            return False
        if len_s2 < len_s1:
            s1, s2 = s2, s1
            len_s1, len_s2 = len_s2, len_s1
        # prev line
        dp = [False for _ in range(len_s2 + 1)]

        # init the bot right to true since we doing bottom up
        dp[len_s2] = True

        # bot right to left to up
        for i in range(len_s1, -1, -1):
            dp_prev = True
            for j in range(len_s2, -1, -1):
                # if you are not at the end of the string (s1 or s2) do this
                # s [i + j] is the combined string pointer index
                # note: remember to check the bot and right path (aka theres is a way s1 or s2 is viable)
                # to make sure the rest of the string is valid since we building it up
                temp_res = False
                if i < len_s1 and s1[i] == s3[i + j] and dp[j]:
                    temp_res = True
                if j < len_s2 and s2[j] == s3[i + j] and dp[j + 1]:
                    temp_res = True
                    dp[j] = temp_res
                    dp_prev = dp[j]

        return dp[0]
