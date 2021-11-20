# https://leetcode.com/problems/product-of-array-except-self/
# tags: #array, #amazon, #prefix_sum
#
# Solution: Two pass
# The first loop gets the product before the element and the second loop gets the product after the element.
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        cum = 1

        for i, num in enumerate(nums):
            output[i] = cum
            cum *= nums[i]

        cum = 1
        for i in range(n - 1, -1, -1):
            output[i] *= cum
            cum *= nums[i]

        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf(nums=[1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
