# https://leetcode.com/problems/kth-largest-element-in-an-array/
# tags: #array, #divide_and_conquer, #heap, #quickselect, #sorting
#
# Solution #1: Sort nums descending and then get the kth number
# Time complexity: O(n*log(n)), Space complexity: O(1)
#
# Solution #2: Convert input nums array into a max-heap that will store kth largest values
# Time complexity: O(n*log(k)), Space complexity: O(k)
#
# Solution #3: The best approach to this problem is to use the selection algorithm (based on partition method).
# To improve the initial approach we will need to randomize the input, so that even when the worst case input
# would be provided the algorithm wouldn't be affected
# Time complexity: O(n), Space complexity: O(1)
import heapq
import random
from typing import List


class Solution:
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        gt = [n for n in nums if n > pivot]
        lt = [n for n in nums if n < pivot]
        eq = [n for n in nums if n == pivot]

        if len(gt) >= k:
            return self.findKthLargest_quickselect(gt, k)
        elif k - len(gt) <= len(eq):
            return eq[0]
        else:
            return self.findKthLargest_quickselect(lt, k - len(gt) - len(eq))


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest_quickselect(nums=[3, 2, 1, 5, 6, 4], k=2))  # 5
    print(sol.findKthLargest_quickselect(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))  # 4
