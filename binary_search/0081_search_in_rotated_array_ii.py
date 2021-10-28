# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# tags: #array, #binary_search
#
# Solution: Binary Search
# Problem similar to "33. Search in Rotated Sorted Array" dealing with duplicates
# We can have nums[left] == nums[mid] and in that case, the first half could be out of order
# (i.e. NOT in the ascending order, e.g. [3 1 2 3 3 3 3]) and we have to deal this case separately.
# In that case, it is guaranteed that nums[right] also equals to nums[mid], so what we can do is to check
# if nums[mid]== nums[left] == nums[right] before the original logic, and if so,
# we can move left and right both towards the middle by 1
# Time Complexity: O(log(n)) - Ω(n), Space complexity: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return True

            if nums[left] == nums[middle] == nums[right]:
                left += 1
                right -= 1
            elif nums[middle] <= nums[right]:  # pivot (min_value) is in the left half
                if nums[middle] < target <= nums[right]:  # target is in range (mid, last]
                    left = middle + 1
                else:
                    right = middle - 1
            else:  # pivot is in the right half
                if nums[left] <= target < nums[middle]:  # target is in range [first, mid)
                    right = middle - 1
                else:
                    left = middle + 1

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))  # True
    print(sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))  # False
    print(sol.search(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2))  # True
