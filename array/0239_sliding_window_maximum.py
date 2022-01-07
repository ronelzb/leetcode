# https://leetcode.com/problems/sliding-window-maximum/
# tags: #heap, #monotonic_queue, #queue, #sliding_window
#
# Solution: Decreasing double ended queue
# Use the idea of decreasing deque: on each moment of time we will keep only decreasing numbers in it.
# Process numbers one by one, keeping indexes in our stack:
# * For each number visited, delete the elements at the head of the queue are older than k.
# * Then, we will find all numbers less than the visited number in the queue and delete them
# * Append, the index of the visited number and append the number at the head of the queue
# Time complexity: O(n), Space complexity O(k)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i in range(len(nums)):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)
            if i >= k - 1: result.append(nums[queue[0]])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [3,3,5,5,6,7]
