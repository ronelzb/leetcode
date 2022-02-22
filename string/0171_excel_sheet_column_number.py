# https://leetcode.com/problems/excel-sheet-column-number/
# tags: #math, #numbers, #string, #top_interview_questions
#
# Solution: Map/Reduce
# We iterate through the chars in the input, and we want to take whatever is stored in res already,
# multiply it by 26.
# Time complexity: O(n), Space complexity: O(n)
from functools import reduce


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda a, b: a * 26 + b, [ord(c) - 64 for c in columnTitle])


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber(columnTitle="A"))  # 1
    print(sol.titleToNumber(columnTitle="AB"))  # 28
    print(sol.titleToNumber(columnTitle="ZY"))  # 701
    print(sol.titleToNumber(columnTitle="FXSHRXW"))  # 2147483647
