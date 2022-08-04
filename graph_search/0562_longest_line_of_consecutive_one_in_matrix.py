# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# tags: #dp, #google, #matrix
#
# Solution: DP
# Instead of doing a traditional graph search we can optimize the search using an
# additional dictionary to convert the matrix into 1 dimensional lists of 0's and 1's
# We scan from left to right, top to bottom, adding each element's value to their respective 4 groups.
# As we visited in reading order, our lines will be appended to in that order.
# For the max score, we keep track of the number of 1's we've seen before.
# If we see a 1, we add to our count and update our answer.
# Time complexity: O(m*n), Space complexity: O(m*n)
from collections import defaultdict
from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        def score(line: List[int]) -> int:
            sc = count = 0
            for x in line:
                if x > 0:
                    count += 1
                    sc = max(sc, count)
                else:
                    count = 0
            return sc

        groups = defaultdict(list)
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                groups[(0, r)] += [val]
                groups[(1, c)] += [val]
                groups[(2, r+c)] += [val]
                groups[(3, r-c)] += [val]

        return max(map(score, groups.values()))


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestLine(mat=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]))  # 3
    print(sol.longestLine(mat=[[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]))  # 4
