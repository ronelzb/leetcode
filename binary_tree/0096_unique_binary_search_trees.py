# https://leetcode.com/problems/unique-binary-search-trees/
# tags: #bst, #dp, #math, #microsoft
#
# Great explanation at:
# https://leetcode.com/problems/unique-binary-search-trees/discuss/1565533/Java-Simple-and-Clean-DP-solution-w-detailed-example-or-Beats-100-or-TC%3A-O(N2)-SC%3A-O(N)
#
# Solution 1: Dynamic Programming
# Time complexity: O(n^2), Space complexity O(n)
#
# Solution 2: Mathematical deduction: Catalan numbers
# Time complexity: O(n), Space complexity O(1)
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

    def numTrees_math(self, n: int) -> int:
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) // (i + 2)
        return c


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees_math(n=3))  # 5
