# https://leetcode.com/problems/sqrtx/
# tags: #binary_search, #math, #top_interview_questions
#
# There are 2 possible solutions for this problem:
# Solution 1: Using only integer division for the Newton method
# https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
# https://en.wikipedia.org/wiki/Newton%27s_method
# https://leetcode.com/problems/sqrtx/discuss/359172/Python-Newton-Solution
# Time complexity: O(log(log(n))), Space complexity: O(1)
#
# Solution 2: Binary search
# Use sorted numeric property to find the largest number, which in this case will be the binary search
# upper bound
# Time complexity: O(log(n)), Space complexity: O(1)
class Solution:
    def mySqrt_newton(self, x: int) -> int:
        x_prev = x
        x_current = x / 2
        precision = .1
        while abs(x_prev - x_current) > precision:
            x_prev = x_current
            x_current = (x_current + x / x_current) / 2

        return int(x_current)

    def mySqrt_bs(self, x: int) -> int:
        left, right, res = 1, x, 0

        while left <= right:
            middle = (left + right) // 2
            if middle <= x // middle:
                left = middle + 1
                res = middle
            else:
                right = middle - 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt_newton(x=10))  # 3
