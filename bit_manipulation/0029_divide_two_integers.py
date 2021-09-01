# https://leetcode.com/problems/divide-two-integers/
# tags: #bit_manipulation, #math
#
# We can come up with several solutions for this problem, 2 of the most popular are explained below. In any case,
# we need to handle edge case -2^31 / 1
#
# Solution 1: Bit manipulation
# * Handle sign at the end, keep unsigned values for shifts
# * Iterate until a is greater than b, use a - b >= 0 to handle overflow
# * Find the largest multiple so that (divisor * multiple <= dividend)
# whereas we are moving with stride 1, 2, 4, 8, 16...2^n for performance reason
# * At the end, check if the result is positive or negative
# Realize that a-b >= 0 is not the same as a >= b when overflow happens
# Time complexity: O(log(n)^2), Space complexity: O(1)
#
# Solution 2: Bit manipulation enhanced
# * Handle sign at the end, keep unsigned values for shifts
# * Iterate over each possible factors from 1 to 2^31
# * Is it possible to reduce "a" up to a >> x, such that a >> x is still grater than b ?, update the quotient
# * At the end, check if the result is positive or negative
# Realize that a-b >= 0 is not the same as a >= b when overflow happens
# Time complexity: O(32) => O(1), Space complexity: O(1)
#
# Solution 2: Binary search
# Use sorted numeric property to find the largest number, which in this case will be the binary search
# upper bound
# Time complexity: O(log(n)), Space complexity: O(1)
class Solution:
    def divide1(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a, b, res = abs(dividend), abs(divisor), 0
        while a - b >= 0:
            x = 0
            while a - (b << x << 1) >= 0:
                x += 1
            res += 1 << x
            a -= b << x

        return res if (dividend > 0) == (divisor > 0) else -res

    def divide2(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(32, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x

        return res if (dividend > 0) == (divisor > 0) else -res


if __name__ == "__main__":
    sol = Solution()
    print(sol.divide1(dividend=10, divisor=3))  # 3
