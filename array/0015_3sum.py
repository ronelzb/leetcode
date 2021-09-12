# https://leetcode.com/problems/3sum/
# #array, #sorting, #two_pointers
#
# Approach: Sorting + 2 sum
# The idea is to sort an input array and then run through all indices of a possible first element of a triplet.
# For each possible first element we make a standard bi-directional 2Sum traversal of the remaining part of the array.
# Also we want to skip equal elements to avoid duplicates in the answer without making a set like that.
#
# Time complexity: O(n^2), Space complexity: O(1)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        if n < 3:
            return result

        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]

                if triplet_sum < 0:
                    left += 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # move left and right until next value is different
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
