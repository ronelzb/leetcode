# https://leetcode.com/problems/word-break-ii/
# tags: #backtracking, #dp, #hash_table, #trie
#
# Solution 1: Backtracking
# 1.Every time, we check whether s starts with a word. If so, we check whether the substring s[len(word):]
# starts with a word, etc.
# 2.sub_list keeps calling until we hit the last word. If the last word is in the dict, we append it to res.
# The last word is dog ==> res = [ "dog"]
# 3.Then we return to sub_list = backtracking(s[len(word):], remaining_words, memo) appending the word that
# starts with s. This step is the important one concatenating what backtracking is returning
# s = "sanddog" because we start with "cat" (cat is the first word in the dict) and "cat" leads to "sand".
# word = "sand", item = "dog", res = ["sand dog"]
# memo ={'dog': ['dog'], "sanddog":["sand dog"] }
#
# Why using memo?
# We always recurse to the last word in the string and backtrack, so storing all possible combinations of the substring
# in the memo saves time for the next iteration of the whole string.
# For example, "catsanddog," if we don't store "dog," then we have to iterate through the dictionary
# Time complexity: O(2^n), Space complexity O(n^2)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtracking(sub_string: str, memo: dict) -> List[str]:
            if sub_string in memo: return memo[sub_string]
            if not sub_string: return []
            res = []

            for word in wordDict:
                if sub_string == word:
                    res.append(word)
                elif sub_string.startswith(word):
                    sub_list = backtracking(sub_string[len(word):], memo)
                    res.extend([word + " " + item for item in sub_list])

            memo[sub_string] = res
            return res

        return backtracking(s, {})


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
    # ["cats and dog","cat sand dog"]

    print(sol.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
    # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
