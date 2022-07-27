# https://leetcode.com/problems/find-k-closest-elements/
# tags: #array, #binary_search #facebook, #heap, #sorting, #two_pointers
#
# Solution 1: Heap
# Keep a heap of length k and for each new incoming value from the array
# compare it against the smallest (first) value of the heap
# At the end return the resulting heap with ascending order
# Time Complexity: O(n*log(k)), Space complexity: O(k)
#
# Solution 2: Two pointers
# Initialize two pointers: left and right as the boundaries of the array
# Keep reducing the window size between left and right until it becomes exactly equals to k
# To know which pointer to update we just use the formula abs(arr[left] - x) <= abs(arr[right] - x)
# If this is true we narrow down right as left is nearest to x according to the problem constraints
# Time Complexity: O(n), Space complexity: O(1)
import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not k:
            return arr

        n = len(arr)
        closest_nums = []
        for i in range(k):
            heapq.heappush(closest_nums, arr[i])

        for i in range(k, n):
            if (abs(arr[i] - x) < abs(closest_nums[0] - x)
                    or (abs(arr[i] - x) == abs(closest_nums[0] - x) and arr[i] < closest_nums[0])):
                heapq.heappushpop(closest_nums, arr[i])

        return sorted(closest_nums)

    def findClosestElements_twoPointers(self, arr: List[int], k: int, x: int) -> List[int]:
        if not k:
            return arr

        left, right = 0, len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1

        return arr[left: right + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements_twoPointers(arr=[5, 6, 7, 8, 9], k=3, x=7))  # [6,7,8]
    print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))  # [1,2,3,4]
    print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))  # [1,2,3,4]
