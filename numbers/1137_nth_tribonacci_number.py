# https://leetcode.com/problems/n-th-tribonacci-number/
# tags: #dp
#
# Solution 1: Recursion
# Custom fibonacci to handle 3-tier recursion
# Time Complexity: O(3^n), Space complexity: O(n)
#
# Solution 2: Dynamic Programming
# Memoize previous results to calculate current
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 3: Dynamic Programming (no additional Space)
# As previous solution but using 3 variables to store current and previous results
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n <= 2: return 1
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

    def tribonacci_dp(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]

    def tribonacci_dp_no_space(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci_dp_no_space(n=25))  # 4
