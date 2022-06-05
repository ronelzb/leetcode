# https://leetcode.com/problems/word-break/
# tags: #dp, #hash_table, #string, #trie
#
# Solution: Dynamic Programming
# Instead of saving an array of booleans we will take a different approach:
# Let's keep an array of indexes of last seen group of words and for each incoming new character
# we will iterate every previous finding and check if it fits
#
# For example: s='leetcode', wordDict=['leet', 'code']
# At first, the starts array will be initialized with 0 (empty)
# Then at i=3, s[0: 4] word 'leet' will match, and we append index 4
# Eventually, at i=7, s[4: 8] word 'code' will match, and we append index 8
# At the end, we have found that s contains all words in wordDict
# Time complexity: O(n^3), Space complexity: O(n)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = {word for word in wordDict}

        starts = [0]
        n = len(s)
        for i in range(n):
            for j in starts:
                if s[j:i + 1] in word_set:
                    starts.append(i + 1)
                    break

        return starts[-1] == n


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak( s="leetcode", wordDict=["leet", "code"])
    assert not sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    assert sol.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"])
