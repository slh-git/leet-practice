# NOTE: u got tree, go left for option to keep ptr in repeatable pool
# got right and the curr ptr is purge from teh poo
#       for ex: go left if u want to repeat 2 again, go right if u no longer let 2
#               repeat
from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        # i: ptr to curr number to add / ban
        # curr combo = curr progress
        def dfs(i, curr_combo, curr_sum):
            if i >= len(nums) or curr_sum > target:
                return
            if curr_sum == target:
                # NOTE: REMEMBER THIS CAUSE UR VALUE WILL DISAPPEAR
                out.append(curr_combo.copy())
                return
            # 1 turn of repeat of curr candidate allowed
            curr_combo.append(nums[i])
            dfs(i, curr_combo, curr_sum + nums[i])
            # reset
            curr_combo.pop()
            # now without the current candidate repeating again
            dfs(i + 1, curr_combo, curr_sum)

        dfs(0, [], 0)
        return out
