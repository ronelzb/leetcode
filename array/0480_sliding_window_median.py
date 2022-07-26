# https://leetcode.com/problems/sliding-window-median/
# tags: #array, #hash_table, #sliding_window, #heap
#
# Solution: Double heaps + sliding window
# https://leetcode.com/problems/sliding-window-median/discuss/394302/Python-clean-solution-(easy-to-understand)
# Time complexity:(n*log(k)), Space complexity: O(k)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        if not k or k > n:
            return []

        small, large = [], []

        for i in range(k):
            if len(small) == len(large):
                heapq.heappush(large, -heapq.heappushpop(small, -nums[i]))
            else:
                heapq.heappush(small, -heapq.heappushpop(large, nums[i]))

        medians = [(large[0] - small[0]) / 2.0 if k % 2 == 0 else float(large[0])]

        idx_to_remove = defaultdict(int)
        for i in range(k, n):
            heapq.heappush(small, -heapq.heappushpop(large, nums[i]))

            num_to_remove = nums[i - k]
            if num_to_remove > -small[0]:
                heapq.heappush(large, -heapq.heappop(small))

            idx_to_remove[num_to_remove] += 1
            while small and idx_to_remove[-small[0]] > 0:
                idx_to_remove[-small[0]] -= 1
                heapq.heappop(small)

            while idx_to_remove[large[0]] > 0:
                idx_to_remove[large[0]] -= 1
                heapq.heappop(large)

            if k % 2 == 0:
                medians.append((large[0] - small[0]) / 2.0)
            else:
                medians.append(float(large[0]))

        return medians


if __name__ == '__main__':
    sol = Solution()
    print(sol.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [1.0,-1.0,-1.0,3.0,5.0,6.0]
    # print(sol.medianSlidingWindow(nums=[1, 2, 3, 4, 2, 3, 1, 4, 2], k=3))  # [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
