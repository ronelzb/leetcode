# https://leetcode.com/problems/reverse-words-in-a-string/
# tags: #string, #two_pointers
#
# Solution 1: Two pointers
# Traverse the string finding the starting/ending characters delimited by trailing spaces
# Time Complexity: O(n), Space complexity: O(n)
#
# Solution 2: Built-in solution
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        start, n = 0, len(s)
        prev_chart = False
        result = []

        for i, c in enumerate(s):
            if not prev_chart and c.isalnum():
                prev_chart = True
                start = i
            elif prev_chart and not c.isalnum():
                prev_chart = False
                result.insert(0, s[start: i])

        if prev_chart: result.insert(0, s[start: n])
        return " ".join(result)

    def reverseWords_builtin(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords_builtin(s="a good   example"))  # "example good a"
    print(sol.reverseWords_builtin(s="EPY2giL"))  # "EPY2giL"
    print(sol.reverseWords_builtin(s=" asdasd df f"))  # "f df asdasd"
