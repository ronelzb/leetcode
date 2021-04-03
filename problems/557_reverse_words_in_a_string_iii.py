from typing import List
from math import ceil


class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        current_word = ""

        for i in range(len(s)):
            current_char = s[i]

            if current_char == " ":
                s = s[:start] + current_word + s[i:]
                start = i + 1
                current_word = ""
            else:
                current_word = current_char + current_word

        s = s[:start] + current_word

        return s


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert sol.reverseWords("God Ding") == "doG gniD"
