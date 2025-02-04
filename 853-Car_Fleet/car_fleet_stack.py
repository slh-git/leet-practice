from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        # Iterate backwards (target-x)/speed to check how many steps needed to reach target
        for p, s in sorted(pair)[::-1]:  # NOTE: reversed
            stack.append((target - p) / s)
            # NOTE: if the second car behind is faster than the car ahead keep only the car in the most front
            # because the car behind's speed be fluctuating
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
