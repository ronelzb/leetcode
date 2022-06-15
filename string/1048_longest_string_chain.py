# https://leetcode.com/problems/longest-string-chain/
# tags: #array, #dp, #hash_table, #string, #two_pointers
#
# Solution: Dynamic Programming
# For each word in sorted words, loop on all possible previous word with 1 letter missing.
# If we have seen the previous word, update the longest chain for the current word.
# Time complexity: O(n*log(n)+n*s*s) s for inner loop and string generation,
# Space complexity: O(n*s)=s for creating prev, n times
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1

        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    res = max(res, dp[word])

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]))  # 4
    print(sol.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # 5
    print(sol.longestStrChain(words=["abcd", "dbqca"]))  # 1
