# https://leetcode.com/problems/plus-one/
# tags: #array, #math, #top_interview_questions
#
# Solution 1: Carry from right to left
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i, n = 1, len(digits)
        carry = 1
        while carry > 0 and i <= n:
            num = digits[n - i] + 1
            carry = num // 10
            digits[n - i] = num % 10
            i += 1

        if carry > 0: digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # [1,2,4]
    print(sol.plusOne([9]))  # [1,0]
