# https://leetcode.com/problems/house-robber/
# tags: #array, #blind_75_must_do, #dp, #top_interview_questions
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_amount = [0] * n
        max_amount[0] = nums[0]

        for i in range(1, n):
            prev = max_amount[i - 2] if i > 1 else 0
            max_amount[i] = max(max_amount[i - 1], prev + nums[i])

        return max_amount[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob(nums=[1, 2, 3, 1]))  # 4
