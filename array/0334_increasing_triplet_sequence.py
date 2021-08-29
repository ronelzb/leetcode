# https://leetcode.com/problems/increasing-triplet-subsequence/
# tags: #array, #greedy
#
# Intuition: Keep track of small (first) and middle (second) numbers when of the subsequence.
# If we find a value that is bigger than both we return True
#
# Time complexity: O(n), Space complexity: O(1)
import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, large = sys.maxsize, sys.maxsize

        for n in nums:
            if n <= small:
                small = n
            elif n <= large:
                large = n
            else:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))  # True
    print(sol.increasingTriplet(nums=[5, 4, 3, 2, 1]))  # False
