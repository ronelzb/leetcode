# https://leetcode.com/problems/edit-distance/
# tags: #dp, #string
#
# Great Explanation at:
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# Levenshtein distance:
# https://en.wikipedia.org/wiki/Levenshtein_distance
#
# Solution 1: Dynamic Programming
# Consider from the last position of the two strings:
# 1. Base case: word1 = "" or word2 = "" => return length of other string
# 2. Case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
# 3. Case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing any of the other string
# depending on the current operation
# Time Complexity: O(m*n), Space complexity: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance(word1="horse", word2="ros"))  # 3
    print(sol.minDistance(word1="intention", word2="execution"))  # 5
    print(sol.minDistance(word1="intention", word2=""))  # 9
