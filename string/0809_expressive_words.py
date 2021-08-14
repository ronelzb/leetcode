# https://leetcode.com/problems/expressive-words/
# tags: #array, #google, #string, #two_pointers
from typing import List


class Solution:
    # Loop through all words. check_stretchy(s, word) checks if word is stretchy to s
    # In check_stretchy function, use two pointer:
    # If s[i] == word[j], i+=1, j+=1
    # Else If s[i - 2] == s[i - 1] == s[i] or s[i - 1] == S[i] == s[i + 1], i+=1
    # Time complexity: O(n*max(len(s), len(word))) n=len(words), Space complexity: O(1)
    def expressiveWords(self, s: str, words: List[str]) -> int:
        n, stretchy = len(s), 0

        def check_stretchy(word):
            m = len(word)
            j = 0

            for i in range(n):
                if j < m and s[i] == word[j]:
                    j += 1
                elif s[i - 1: i + 2] != s[i] * 3 != s[i - 2: i + 1]:
                    return False

            return j == m

        for w in words:
            if check_stretchy(w):
                stretchy += 1

        return stretchy


if __name__ == "__main__":
    sol = Solution()

    print(sol.expressiveWords(s="heeellooo", words=["hello", "hi", "helo"]))  # 1
    print(sol.expressiveWords(s="zzzzzyyyyy", words=["zzyy", "zy", "zyy"]))  # 3
