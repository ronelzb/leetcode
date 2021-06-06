# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for i, num in enumerate(nums):
            remaining = target - nums[i]
            if remaining in num_to_idx:
                return [num_to_idx[remaining], i]

            num_to_idx[nums[i]] = i

        return []


if __name__ == "__main__":
    sol = Solution()

    # assert sol.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
