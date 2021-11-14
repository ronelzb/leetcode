# https://leetcode.com/problems/gray-code/
# tags: #backtracking, #bit_manipulation, #math
#
# Solution: Bit manipulation + backtracking
# from up to down, then left to right
#     0   1   11  110
#             10  111
#                 101
#                 100
#
#     start:      [0]
#     i = 0:      [0, 1]
#     i = 1:      [0, 1, 3, 2]
#     i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
# Time complexity: O(2^n), Space complexity O(2^n)
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n):
            results += [x | (1 << i) for x in results[::-1]]
        return results


if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(n=4))  # [0,1,3,2]
