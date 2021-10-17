# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=146466059993201&ppid=454615229006519&practice_plan=0
# E.g: [5,3,9,4,1,8,6,2,7]
# Let's start with student 5. Student 5 gives the book to 1 and 1 gives back to 5:
# * Group 1: 5->1-> (back to 5)
#
# For student 3 group will be like:
# * Group 2: 3->9->7->6->8->2-> (back to 3)
#
# Student 4 will sign only the book he/she own.
# Time Complexity: O(n), Space complexity: O(n)
from typing import List


class Solution:
    def findSignatureCounts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        visited = set()

        for idx in arr:
            if idx not in visited:
                passing_round = set()
                while idx not in visited:
                    passing_round.add(idx)
                    visited.add(idx)
                    idx = arr[idx - 1]

                for k in passing_round:
                    result[k - 1] = len(passing_round)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findSignatureCounts(arr=[2, 1]))  # [2, 2]
    print(sol.findSignatureCounts(arr=[1, 2]))  # [1, 1]
    print(sol.findSignatureCounts(arr=[5, 3, 9, 4, 1, 8, 6, 2, 7]))  # [2, 6, 6, 1, 2, 6, 6, 6, 6]
