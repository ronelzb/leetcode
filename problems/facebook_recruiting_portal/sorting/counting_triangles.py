# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=720422605157879&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time complexity: O(n*k*log(k)) k=3 => O(n), Space complexity O(n)
from typing import List


class Solution:
    def countDistinctTriangles(self, arr: List[tuple]):
        unique_triangles = set()
        for triangle in arr:
            unique_triangles.add(tuple(sorted(triangle)))
        return len(unique_triangles)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinctTriangles(arr=[(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]))  # 3
    print(sol.countDistinctTriangles(arr=[(3, 4, 5), (8, 8, 9), (7, 7, 7)]))  # 3
    print(sol.countDistinctTriangles(arr=[(2, 2, 3), (3, 2, 2), (2, 5, 6)]))  # 2
    print(sol.countDistinctTriangles(arr=[(8, 4, 6), (100, 101, 102), (84, 93, 173)]))  # 3
    print(sol.countDistinctTriangles(arr=[(5, 8, 9), (5, 9, 8), (9, 5, 8), (9, 8, 5), (8, 9, 5), (8, 5, 9)]))  # 1
