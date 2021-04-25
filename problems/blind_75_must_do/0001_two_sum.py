# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_values = {nums[0]: 0}

        for i in range(1, len(nums)):
            current = nums[i]
            remaining = target - current

            if remaining in visited_values:
                return [visited_values[remaining], i]

            visited_values[current] = i


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum(nums=[2, 11, 15, 7], target=9) == [0, 3]
    assert sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert sol.twoSum(nums=[3, 3], target=6) == [0, 1]
