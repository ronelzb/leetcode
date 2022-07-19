# https://leetcode.com/problems/minimum-time-difference/
# tags: #array, #google, #math, #string, #sorting
#
# Solution: Sorting
# Convert each timestamp to its equivalent in minutes and sort the resulting array
# The required minimum difference must be a difference between two adjacent elements in the circular array,
# so the last element is "adjacent" to the first.
# Time complexity: O(n*log(n)), Space complexity: O(n)
import sys
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timestamps = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        timestamps.append(timestamps[0] + 1440)
        min_difference = sys.maxsize

        for i in range(1, len(timestamps)):
            min_difference = min(min_difference, timestamps[i] - timestamps[i - 1])

        return min_difference


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinDifference(timePoints=["23:59", "00:00"]))  # 1
    print(sol.findMinDifference(timePoints=["00:00", "04:00", "22:00"]))  # 120
