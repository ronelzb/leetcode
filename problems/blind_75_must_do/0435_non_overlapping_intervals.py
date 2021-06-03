# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


class Solution:
    # Idea: https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python
    # Greedy scheduling algorithm:
    # Which interval would be the best first (leftmost) interval to keep? One that ends first,
    # as it leaves the most room for the rest.
    # At each interval we'll check current end with the next scheduling start, if overlaps then it can be removed
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlap_intervals = 0
        end = float("-inf")

        for interval in sorted(intervals, key=lambda elem: elem[1]):
            if end <= interval[0]:
                end = interval[1]
            else:
                overlap_intervals += 1

        return overlap_intervals


if __name__ == "__main__":
    sol = Solution()

    assert sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]) == 0
