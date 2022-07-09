# https://leetcode.com/problems/jump-game-vi/
# tags: #array, #dp, #heap, #monotonic_queue, #queue, #sliding_window
#
# Solution: Dynamic Programming + Monotonic Queue
# 1. Initialize a deque score, which represents the values between nums[i] and nums[i+k]
# in monotonic decreasing order
# 2. For each item in nums:
#   * Pop all indexes smaller than i-k from the left
#   * Remove all those values smaller than the current cost to jump (first value of the queue + nums[i])
#   to make the queue monotonically decreasing
#   * Push the cost and i to the end of the deque
# 3. Return the last value of the deque which is the maximum score found.
# Time complexity: O(n), Space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while queue and queue[0][1] + k < i:
                queue.popleft()
            cost = nums[i] + queue[0][0]

            while queue and cost >= queue[-1][0]:
                queue.pop()

            queue.append((cost, i))

        return queue[-1][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))  # 7
    print(sol.maxResult(nums=[10, -5, -2, 4, 0, 3], k=3))  # 17
    print(sol.maxResult(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2))  # 0
