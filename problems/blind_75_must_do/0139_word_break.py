# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set()
        for word in wordDict:
            word_set.add(word)

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
