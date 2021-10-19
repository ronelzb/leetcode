# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=510655302929581&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n*log(n)), Space complexity: O(k)
import functools
import heapq
from typing import Optional, List


class Solution:
    def findMaxProduct(self, arr: Optional[List]) -> Optional[List]:
        heap, n, k = [], 0, 3
        for i, num in enumerate(arr):
            if n < k:
                heapq.heappush(heap, num)
                n += 1
                arr[i] = -1 if n < k else functools.reduce(lambda a, b: a * b, heap)
            else:
                heapq.heappushpop(heap, num)
                arr[i] = functools.reduce(lambda a, b: a * b, heap)

        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxProduct(arr=[1, 2, 3, 4, 5]))  # [-1, -1, 6, 24, 60]
