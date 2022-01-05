# https://leetcode.com/problems/palindrome-partitioning/
# tags: #backtracking, #dp, #string
#
# Solution: Backtracking
# Idea: Make a backtracking (dfs) variation.
# At each iteration validate if the current substring is a palindrome using a dp matrix
# If we use a 2d array to keep track of any string we have scanned so far, with an addition pair,
# we can determine whether it's palindrome or not by looking at that pair
# e.g: For 'abca', a (first) == a (last) and b != c then continue
# Time complexity: O(n^2+2^n), Space complexity: O(n^2)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palindromes = []
        dp = [[False] * n for _ in range(n)]

        def backtracking(pos: int, weave: List[str]) -> None:
            if pos == n:
                palindromes.append(weave)

            for i in range(pos, n):
                # print(pos, i, "\n", "\n".join(["\t".join(map(str, row)) for row in dp]), "\n")
                if s[i] != s[pos] or (i - 1 > pos and not dp[pos + 1][i - 1]):
                    continue

                dp[pos][i] = True
                backtracking(i + 1, weave + [s[pos:i + 1]])

        backtracking(0, [])
        return palindromes


if __name__ == "__main__":
    sol = Solution()

    assert sol.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
