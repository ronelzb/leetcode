# https://leetcode.com/problems/pascals-triangle/
# tags: #dp, #top_interview_questions
#
# Solution: Dynamic Programming
# Any row can be constructed using the offset sum of the previous row.
# Time complexity: O(n^2), Space complexity O(1)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j - 1] + result[i-1][j]

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(numRows=5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
