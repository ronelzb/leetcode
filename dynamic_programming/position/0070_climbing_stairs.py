# https://leetcode.com/problems/climbing-stairs/
# tags: #dp, #math, #top_interview_questions
#
# Solution 1: Recursion with memoization
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 2: Fibonacci number
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 3: Dynamic Programming
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def climbStairs_rm(self, n: int) -> int:
        def recursion(i) -> int:
            if i > n: return 0
            elif i == n: return 1
            elif memo[i] > 0: return memo[i]

            memo[i] = recursion(i + 1) + recursion(i + 2)
            return memo[i]

        memo = [0] * (n + 1)
        return recursion(0)

    def climbStairs_fib(self, n: int) -> int:
        if n < 3: return n
        first = 1
        second = 2

        for i in range(2, n):
            third = first + second
            first, second = second, third
        return second

    def climbStairs_dp(self, n: int) -> int:
        if n < 3:
            return n

        permutations = [0] * n
        permutations[0] = 1
        permutations[1] = 2

        for i in range(2, n):
            permutations[i] = permutations[i - 1] + permutations[i - 2]

        return permutations[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs_fib(n=4))  # 5
