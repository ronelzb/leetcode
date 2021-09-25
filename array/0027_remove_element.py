# https://leetcode.com/problems/remove-element/
# tags: #array, #two_pointers
#
# Solution: Two pointers
# Have a slow and fast pointers, update nums[slow] when nums[fast] != value
# To optimize the code update in-place nums[slow] when fast > slow
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n != val:
                if i > k:
                    nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement(nums=[3, 2, 2, 3], val=3))  # 2, nums = [2,2,_,_]
    print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # 5, nums = [0,1,3,0,4,_,_,_]
