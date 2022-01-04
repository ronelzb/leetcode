# https://leetcode.com/problems/complement-of-base-10-integer/
# tags:
#
# Solution: Bit Manipulation + Math
# An efficient way to calculate one's complement in base 10 is:
# * Find the number of bits in the given integer.
# * XOR the given integer with 2 ^ number_of_bits - 1
# Time complexity: O(log(n)), Space complexity O(1)
import math


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bits = math.floor(math.log(n, 2)) + 1
        return n ^ ((1 << bits) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.bitwiseComplement(n=5))  # 2
    print(sol.bitwiseComplement(n=7))  # 0
    print(sol.bitwiseComplement(n=10))  # 5
    print(sol.bitwiseComplement(n=0))  # 1
