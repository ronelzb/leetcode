# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)

        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
