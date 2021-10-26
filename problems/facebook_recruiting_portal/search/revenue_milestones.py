# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=192049171861831&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n + k*log(n)), Space complexity: O(n)
from typing import List


class Solution:
    def getMilestoneDays(self, revenues: List[int], milestones: List[int]) -> List[int]:
        result = []
        rolling_revenues = [revenues[0]]
        n = len(revenues)

        for i in range(1, n):
            rolling_revenues.append(rolling_revenues[-1] + revenues[i])

        for milestone in milestones:
            left, right = 0, n - 1
            while left <= right:
                middle = (left + right) // 2
                if rolling_revenues[middle] < milestone:
                    left = middle + 1
                else:
                    right = middle - 1

            if n > left >= 0:
                result.append(left + 1)
            else:
                result.append(-1)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.getMilestoneDays(revenues=[100, 200, 300, 400, 500],
                               milestones=[300, 800, 1000, 1400, 1700]))  # [2, 4, 4, 5, -1]

    print(sol.getMilestoneDays(revenues=[700, 800, 600, 400, 600, 700],
                               milestones=[3100, 2200, 800, 2100, 1000]))  # [5, 4, 2, 3, 2]
