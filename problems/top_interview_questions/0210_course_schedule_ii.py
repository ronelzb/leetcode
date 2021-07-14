# https://leetcode.com/problems/course-schedule-ii/
from typing import List


class Solution:
    # Algorithm based on problem 4.7 on Cracking the Interview Code book
    # Also, Kahn's algorithm can be applied as a solution
    # Another idea is to read about topological sort and make a variant of it
    # Idea: Build a dependency tree and the set of courses on a list by the num of courses
    # The dependency tree intersected with the current available courses will dictate if the course
    # does not have any dependency left thus is available to be added.
    # When the course if added we remove it from the set of available courses.
    # Time complexity: O(V + E) V: numCourses, E: len(prerequisites), Space complexity: O(V + E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        courses = set([i for i in range(numCourses)])
        dependency_tree = {i: set() for i in range(numCourses)}
        for c, r in prerequisites:
            dependency_tree[c].add(r)
        course_order = []

        while courses:
            found_course = False
            for course in list(courses):
                requirements = dependency_tree[course]

                if not courses.intersection(requirements):
                    course_order.append(course)
                    courses.remove(course)
                    found_course = True

            if not found_course:
                return []

        # print(course_order)
        return course_order


if __name__ == "__main__":
    sol = Solution()

    assert sol.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
