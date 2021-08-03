# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
from typing import List


class Solution:
    # Solution:
    # https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/944828/Short-DP-solution-with-highly-detailed-step-by-step-explanation
    # Time complexity: O(n^2 * d), Space complexity: O(n * d)
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [float("inf")] * n + [0]

        for day in range(1, d + 1):
            for i in range(n - day + 1):
                max_difficulty, dp[i] = 0, float("inf")
                for j in range(i, n - day + 1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j])
                    dp[i] = min(dp[i], max_difficulty + dp[j + 1])

        return dp[0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))  # 7
