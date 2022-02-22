# https://leetcode.com/problems/roman-to-integer/
# tags: #hash_table, #math, #must_do_easy_questions, #string, #top_interview_questions
#
# Solution: Roman to Int Dictionary
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        n, result = len(s), 0

        for i in range(n - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]

        return result + roman_dict[s[-1]]


if __name__ == "__main__":
    sol = Solution()
    print("III >", sol.roman_to_int("III"))
    print("IV >", sol.roman_to_int("IV"))
    print("IX >", sol.roman_to_int("IX"))
    print("LVIII >", sol.roman_to_int("LVIII"))
    print("MCMXCIV >", sol.roman_to_int("MCMXCIV"))
