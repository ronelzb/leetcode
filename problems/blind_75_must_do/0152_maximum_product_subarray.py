# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_local, min_local, max_product = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            max_local, min_local = max(max_local * nums[i], min_local * nums[i], nums[i]), \
                                   min(max_local * nums[i], min_local * nums[i], nums[i])

            max_product = max(max_local, max_product)

        return max_product


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProduct(nums=[2, 3, -2, 4]) == 6
    assert sol.maxProduct(nums=[-2, -4, -8, 2, 3, -2]) == 768
