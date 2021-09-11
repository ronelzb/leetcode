# https://leetcode.com/problems/4sum/
# tags: #array, #sorting, #two_pointers
#
# Solution: Two for-loops and two pointers
# Follow-up problem from Two Sum and Three Sum
#
# We fix nums[i], nums[j] by iterating the combination of nums[i], nums[j]
#
# By using two pointers, one points to left, the other points to right, remain = target - nums[i] - nums[j]:
# * If nums[left] + nums[right] == remaining, found a quadruplet
# * Else if nums[left] + nums[right] > remaining, Sum is bigger than remain, need to decrease right bound by 1
# * Else increase left bound by 1
#
# Time Complexity: O(n^3), Space complexity: O(1)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = set()
        if n < 4:
            return []

        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1
                remaining = target - nums[i] - nums[j]

                while left < right:
                    if nums[left] + nums[right] == remaining:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > remaining:
                        right -= 1
                    else:
                        left += 1

        return list(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
