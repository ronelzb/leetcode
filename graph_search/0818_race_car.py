# https://leetcode.com/problems/race-car/
# tags: #bfs, #dp, #google, #queue
# Graphical explanation:
# https://leetcode.com/problems/race-car/discuss/227415/Figures-to-make-the-DP-solution-more-straightforward
# Scholar explanation:
# https://leetcode.com/problems/race-car/discuss/124326/Summary-of-the-BFS-and-DP-solutions-with-intuitive-explanation
# Best DP explanation:
# https://leetcode.com/problems/race-car/discuss/246138/java-DP-solution-heavily-commented.
#
# 1. BFS solution
# We can track the car position after all possible movements of the car after n instructions
# since for each position we have two choices: either accelerate or reverse, and
# return smallest n such that the target has been met. To optimize naive run at O(2^n) we need
# to memoize intermediate overlapping states, we just need to be careful of overflowing space
# for large target positions.
# Time complexity: O(target * log(target)), Space complexity: O(target * log(target))
#
# 2. DP bottom-up
# Following @fun4LeetCode explanation: We memoize the minimum steps to get to target at each position i
# We have 3 options at each position to get to the target:
# i. Perfect position to get to i just accelerating (e.g: AAA), which is 1, 3, 7, 15... 2^n - 1
# ii. Car reaches right position to i, reverse facing left and then go back to i
# iii. Car reaches left position to i, reverse again to go back facing right and then go back to i
# Time complexity: O(target * log(target)), Space complexity: O(target)

import sys
from collections import deque


class Solution:
    def racecar_BFS(self, target: int) -> int:
        queue = deque([(0, 1)])  # starts from position 0 with speed 1
        visited = {(0, 1)}
        level = 0

        while queue:
            for _ in range(len(queue)):
                position, speed = queue.popleft()

                if position == target:
                    return level

                nxt = (position + speed, speed << 1)  # accelerate

                if nxt not in visited and 0 < nxt[0] < (target << 1):
                    queue.append(nxt)
                    visited.add(nxt)

                nxt = (position, -1 if speed > 0 else 1)  # reverse

                if nxt not in visited and 0 < nxt[0] < (target << 1):
                    queue.append(nxt)
                    visited.add(nxt)
            level += 1

        return -1

    def racecar_bottomupDP(self, target: int) -> int:
        dp = [sys.maxsize] * (target + 1)
        dp[0] = 0

        for i in range(1, target + 1):
            position, steps = 0, 0

            while position < i:
                steps += 1
                position = (1 << steps) - 1

            if position == i:
                dp[i] = steps
                continue

            dp[i] = steps + 1 + dp[position - i]

            steps -= 1
            position = (1 << steps) - 1

            for j in range(steps):
                reverse = position - ((1 << j) - 1)
                dp[i] = min(dp[i], steps + 1 + j + 1 + dp[i-reverse])

        return dp[target]


if __name__ == "__main__":
    sol = Solution()

    print(sol.racecar_BFS(target=3))  # 2 ("AA")
    print(sol.racecar_BFS(target=4))  # 5 ("AA")
    print(sol.racecar_BFS(target=6))  # 5 ("AAARA")
