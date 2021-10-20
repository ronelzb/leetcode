# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=547645422524434&ppid=454615229006519&practice_plan=0
# Same as LeetCode 295: Find Median from Data Stream:
# https://leetcode.com/problems/find-median-from-data-stream/
# Solution at:
# https://github.com/ronelzb/leetcode/tree/master/array/0295_find_median_from_data_stream.py
# Time Complexity: O(n*log(n)), Space complexity: O(n)
import heapq
from typing import List


class Solution:
    def findMedian(self, arr: List[int]) -> List[int]:
        largest, smallest, median = [], [], []

        for i, num in enumerate(arr):
            heapq.heappush(largest, -heapq.heappushpop(smallest, num))

            if len(smallest) < len(largest):
                heapq.heappush(smallest, -heapq.heappop(largest))

            if len(smallest) > len(largest):
                median.append(smallest[0])
            else:
                median.append((smallest[0] - largest[0]) // 2)

        return median


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedian([5, 15, 1, 3]))  # [5, 10, 5, 4]
