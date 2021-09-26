# https://leetcode.com/problems/decode-ways/
# tags: #dp, #string
#
# Solution 1: Recursion with memoization
# Divide-and-conquer the problem into simpler problems using an array memo to store previous results
# If the current letter is 1 or 27 then concatenate them together
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 2: Dynamic Programming
# Use a dp array of size n + 1 to save subproblem solutions.
# * dp[0] means an empty string will have one way to decode,
# * dp[1] means the way to decode a string of size 1.
# Then check one digit and two digit combination and save the results along the way.
# In the end, dp[n] will be the end result.
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def numDecodings_memo(self, s: str) -> int:
        def num(i) -> int:
            if memo[i] > - 1: return memo[i]
            if s[i] == "0":
                memo[i] = 0
                return memo[i]
            res = num(i + 1)
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')): res += num(i + 2)
            memo[i] = res
            return res

        if not s: return 0
        n = len(s)
        memo = [-1] * (n + 1)
        memo[n] = 1
        return num(0)

    def numDecodings_dp(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        results_table = [0] * (n + 1)
        results_table[0] = results_table[1] = 1

        for i in range(1, n):
            if s[i] != "0":
                results_table[i + 1] += results_table[i]
            if s[i - 1] != "0" and 1 <= int(s[i - 1: i + 1]) <= 26:
                results_table[i + 1] += results_table[i - 1]

        return results_table[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings_memo(s="226"))  # 3
    print(sol.numDecodings_memo(s="12"))  # 2
    print(sol.numDecodings_memo(s="0"))  # 0
    print(sol.numDecodings_memo(s="06"))  # 0
    print(sol.numDecodings_memo(s="10"))  # 1
