# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = []
        number_indexing = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digits_to_letters = []
        for d in digits:
            digits_to_letters.append(number_indexing[int(d) - 2])

        def backtracking(sub_digits, weave):
            if not sub_digits:
                combinations.append(weave)
                return

            for c in sub_digits[0]:
                backtracking(sub_digits[1:], weave + c)

        backtracking(digits_to_letters, "")
        print(combinations)
        return combinations


if __name__ == "__main__":
    sol = Solution()

    assert sol.letterCombinations(digits="23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
