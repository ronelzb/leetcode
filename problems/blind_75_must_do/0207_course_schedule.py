# https://leetcode.com/problems/course-schedule/
# graph cycle detection: https://en.wikipedia.org/wiki/Topological_sorting
from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for c, r in prerequisites:
            graph[c].append(r)
        status = [-1] * numCourses

        def has_cycle(course: int) -> bool:
            if status[course] == 0:
                return True
            if status[course] == 1:
                return False

            status[course] = 0
            for requirement in graph[course]:
                if has_cycle(requirement):
                    return True

            status[course] = 1
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert not sol.canFinish(numCourses=20,
                             prerequisites=[[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]])
