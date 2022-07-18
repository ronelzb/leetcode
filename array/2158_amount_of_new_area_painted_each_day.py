# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# tags: #array, #google, #ordered_set, #segment_tree
#
# Solution: Jumping in 1d array
# * Iterate on intervals
# * For each interval traverse start to end marking each jump value as end
# * In any jump index is already marked skip to the jump value
# Time complexity : O(n+k) k is the length of the interval, Space complexity: O(n+k)
from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        seen = {}
        res = []

        for start, end in paint:
            interval = 0

            while start < end:
                if start in seen:
                    seen[start], start = max(seen[start], end), seen[start]
                else:
                    seen[start] = end
                    interval += 1
                    start += 1

            res .append(interval)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.amountPainted(paint=[[1, 4], [4, 7], [5, 8]]))  # [3,3,1]
    print(sol.amountPainted(paint=[[1, 4], [5, 8], [4, 7]]))  # [3,3,1]
    print(sol.amountPainted(paint=[[1, 5], [2, 4]]))  # [3,3,0]
