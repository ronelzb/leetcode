from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        elif newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        for i in reversed(range(n)):
            if i < n - 1 and newInterval[1] < intervals[i + 1][0] and newInterval[0] > intervals[i][1]:
                intervals.insert(i if newInterval[0] < intervals[i][0] else i + 1, newInterval)
                return intervals
            elif i < n - 1 and newInterval[1] >= intervals[i + 1][0] and newInterval[0] <= intervals[i][1]:
                intervals[i + 1][1] = max(intervals[i + 1][1], newInterval[1])
                intervals[i + 1][0] = min(intervals[i][0], newInterval[0])
                intervals.pop(i)
            elif (intervals[i][0] <= newInterval[0] <= intervals[i][1]) or \
                    (intervals[i][0] <= newInterval[1] <= intervals[i][1]) or \
                    (newInterval[0] <= intervals[i][0] <= newInterval[1]) or \
                    (newInterval[0] <= intervals[i][1] <= newInterval[1]):
                intervals[i][0] = min(intervals[i][0], newInterval[0])
                intervals[i][1] = max(intervals[i][1], newInterval[1])

        return intervals


if __name__ == "__main__":
    sol = Solution()
    assert sol.insert(intervals=[], newInterval=[5, 7]) == [[5, 7]]
    sol.insert(intervals=[[1, 5]], newInterval=[6, 7]) == [[1, 5], [6, 7]]
    sol.insert(intervals=[[4, 5], [6, 7]], newInterval=[1, 2]) == [[1, 2], [4, 5], [6, 7]]
    assert sol.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == \
           [[1, 2], [3, 10], [12, 16]]

    assert sol.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]
    assert sol.insert(intervals=[[1, 3], [6, 9]], newInterval=[0, 6]) == [[0, 9]]

    assert sol.insert(intervals=[[1, 3], [6, 9]], newInterval=[7, 10]) == [[1, 3], [6, 10]]
    assert sol.insert(intervals=[[1, 3], [6, 9]], newInterval=[0, 2]) == [[0, 3], [6, 9]]

    assert sol.insert(intervals=[[1, 5]], newInterval=[0, 6]) == [[0, 6]]
    assert sol.insert(intervals=[[3, 5],[12, 15]], newInterval=[6, 6]) == [[3, 5], [6, 6], [12, 15]]
