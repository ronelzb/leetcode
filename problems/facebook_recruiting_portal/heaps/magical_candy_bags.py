# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=513590792640579&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n*log(n)), Space complexity: O(1)
import heapq
from typing import Optional, List


class Solution:
    def maxCandies(self, arr: Optional[List], k: int) -> int:
        total_candies = 0
        arr = [-x for x in arr]
        heapq.heapify(arr)

        for _ in range(k):
            candies = -heapq.heappop(arr)
            total_candies += candies
            heapq.heappush(arr, -(candies // 2))

        return total_candies


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCandies(arr=[2, 1, 7, 4, 2], k=3))  # 14
    print(sol.maxCandies(arr=[19, 78, 76, 72, 48, 8, 24, 74, 29], k=3))  # 228
