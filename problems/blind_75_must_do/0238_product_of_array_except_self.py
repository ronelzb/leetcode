# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        cum = 1
        for i, num in enumerate(nums):
            res[i] = cum
            cum *= num

        cum = 1
        for i in range(n - 1, -1, -1):
            res[i] *= cum
            cum *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
