# https://leetcode.com/problems/power-of-four/
# tags: #bit_manipulation, #math, #recursion
#
# Solution: Bit manipulation
# We need to check 3 conditions:
# 1. Number is positive.
# 2. Number is power of 2.
# 3. This power of 2 is even power.
# For the second condition we can use x & (x - 1). Number is power of two if it has only one significant bit,
# that is after this operation it must be equal to zero.
# For the last condition we have the pattern, 1, 100, 10000, which in fact results in the following
# bit mask m = 1010101010101010101010101010101.
# Time complexity: O(1), Space complexity: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour(16))  # True
    print(sol.isPowerOfFour(5))  # False
    print(sol.isPowerOfFour(1))  # True
