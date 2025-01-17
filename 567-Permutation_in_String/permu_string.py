class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_check, s2_check = [0] * 26, [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1_check[ord(s1[i]) - ord("a")] += 1
            s2_check[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            matches += 1 if s1_check[i] == s2_check[i] else 0

        # left ptr
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Slide window
            # increment the s2 on the right side
            i = ord(s2[r]) - ord("a")
            s2_check[i] += 1
            # check if equal
            if s1_check[i] == s2_check[i]:
                matches += 1
            elif s1_check[i] == s2_check[i] - 1:
                # means previously s1_check[i] == s2_check[i]: and now s2 has too much
                matches -= 1

            # decrement
            i = ord(s2[l]) - ord("a")
            s2_check[i] -= 1
            if s1_check[i] == s2_check[i]:
                matches += 1
            elif s1_check[i] == s2_check[i] + 1:
                matches -= 1

            l += 1
        return matches == 26
