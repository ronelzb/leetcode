# https://leetcode.com/problems/single-number/
# tags: #array, #bit_manipulation
#
# Solution 1: XOR bit manipulation
# XOR satisfy commutative law and associative law,so 1 ^ 2 ^ 1 equal to (1^1) ^ 2 which is 0 ^ 2
# Time complexity: O(n), Space complexity O(1)
#
# Solution 2: XOR bit manipulation with Python built-in method
# Time complexity: O(n), Space complexity O(1)
#
# Solution 3: Set + sum
# Although this solution uses an additional space with Set it's good for comparison
# Time complexity: O(n), Space complexity O(n)
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    def singleNumber_oneliner(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber_setsum(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber_setsum(nums=[2, 2, 1]))  # 1
    print(sol.singleNumber_setsum(nums=[4, 1, 2, 1, 2]))  # 4
