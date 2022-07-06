# https://leetcode.com/problems/fibonacci-number/
# tags: #dp, #math, #recursion
#
# Solution 1: Recursion
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1
# Time complexity: O(2^n), Space complexity: O(1)
#
# Solution 2: Dynamic Programming
# Bottom-up solution
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 3: Dynamic Programming - No extra space
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def fib_recursion(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib_recursion(n - 1) + self.fib_recursion(n - 2)

    def fib_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n > 0:
            dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def fib_dp2(self, n: int) -> int:
        if n < 2:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return b


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib_dp(n=2))  # 1
    print(sol.fib_dp(n=3))  # 2
    print(sol.fib_dp(n=4))  # 3
