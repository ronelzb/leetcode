# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# tags: #binary_search, #facebook, #heap, #matrix, #sorting, #top_interview_questions
#
# Solution 1: Min heap
# Take the smallest number from the min-heap, if the current iteration equals k returns the number
# If the row of the top element has more elements, add the next element to the min-heap
# Time complexity: O(min(n, k) + k*log(n)), Space complexity: O(n)
#
# Solution 2: Binary Search
# Use a customized matrix binary search
# We will take left as matrix[0][0] and height as matrix[n-1][n-1] where n are the rows in matrix
# Then, find mid and count the elements less than mid in each row
# if count < k means we have to find the greater mid so that count can become equal to k
# else height = mid
# Eventually, return left.
# Time complexity: O(n*log(max-min)), Space complexity: O(1)
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = []

        # We only need to store k row elements
        for i in range(min(n, k)):
            heapq.heappush(h, (matrix[i][0], 0, matrix[i]))


        count = 0
        while h:
            number, i, row = heapq.heappop(h)
            count += 1
            if count == k:
                return number
            if len(row) > i + 1:
                heapq.heappush(h, (row[i + 1], i + 1, row))

        return 0

    def kthSmallestBS(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def less_equals(middle, smaller, larger) -> (int, int, int):
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > middle:
                    larger = min(larger, matrix[row][col])
                    row -= 1
                else:
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1

            return count, smaller, larger

        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            middle = (left + right) // 2
            count, smaller, larger = less_equals(middle, matrix[0][0], matrix[n - 1][n - 1])

            if count == k:
                return smaller
            elif count < k:
                left = larger
            else:
                right = smaller

        return left


if __name__ == "__main__":
    sol = Solution()

    assert sol.kthSmallestBS(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13
    assert sol.kthSmallestBS(matrix=[[-5]], k=1) == -5
    assert sol.kthSmallestBS(matrix=[[1, 2], [1, 3]], k=2) == 1
