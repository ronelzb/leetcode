# https://leetcode.com/problems/single-number-iii/
# tags: #array, #bit_manipulation
#
# Solution: XOR bit manipulation
# The idea is to use XOR to remove all numbers that appear exactly twice.
# Thus, in the first pass, we will XOR all nums in the input array.
# We will be left with XOR of two numbers that appear exactly once. (Let's call these numbers A and B.)
#
# In XOR, a bit is set in the result if both bits at the same locations are different.
# Now find the rightmost set bit in -xor. This will give us the rightmost bit that is different in A & B.
#
# We can now go through all numbers in input array again (second pass) and
# XOR the numbers that have this bit set to 1. This will give us the first number A.
# To get the second number perform xor ^ A.
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        right_set_bit = xor & -xor
        a = 0
        for num in nums:
            if num & right_set_bit != 0:
                a ^= num

        return [a, xor ^ a]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.singleNumber(nums=[1, 2, 1, 3, 2, 5]))  # [3,5]
    print(sol.singleNumber(nums=[2, 1, 2, 3, 4, 1]))  # [3,4]
