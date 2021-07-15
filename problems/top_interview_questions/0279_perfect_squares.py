# https://leetcode.com/problems/perfect-squares/
class Solution:
    # Idea: Knapsack problem variant
    # We can get all perfect square numbers to the n values
    # Then, declare an array of size n + 1 which have the min squares for 0...1...2...n-1...n
    # at each index i we will iterate from the square start to n + 1 finding the min value between
    # the stored current value and index - square + 1 that is previous result
    # Time complexity: O(s * n) s: squares found, Space complexity O(n)
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [n] * (n + 1)
        dp[0] = 0

        for s in squares:
            for i in range(s, n + 1):
                dp[i] = min(dp[i], 1 + dp[i - s])

        return dp[n]


if __name__ == "__main__":
    sol = Solution()

    sol.numSquares(n=12)  # 3
