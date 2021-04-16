from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        i = 0

        while i < n - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
                n -= 1
            else:
                i += 1

        return intervals


if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
