# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
import heapq
from typing import List


class Solution:
    # Ideas from:
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search
    # Solution 1: Using min-heap, space complexity: O(n), time complexity: O(min(n, k) + k*log(n))
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = []

        # We only need to store k row elements
        for i in range(min(n, k)):
            heapq.heappush(h, (matrix[i][0], 0, matrix[i]))

        # Take the smallest number from the min-heap, if the current iteration equals k returns the number
        # If the row of the top element has more elements, add the next element to the min-heap
        count = 0
        while h:
            number, i, row = heapq.heappop(h)
            count += 1
            if count == k:
                return number
            if len(row) > i + 1:
                heapq.heappush(h, (row[i + 1], i + 1, row))

        return 0

    # Solution 2: Using customized matrix binary-search, time complexity: O(n*log(max-min))
    def kthSmallestBS(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            middle = (left + right) // 2
            count, smaller, larger = self.less_equals(matrix, n, middle, matrix[0][0], matrix[n - 1][n - 1])

            if count == k:
                return smaller
            elif count < k:
                left = larger
            else:
                right = smaller

        return left

    def less_equals(self, matrix, n, middle, smaller, larger) -> (int, int, int):
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


if __name__ == "__main__":
    sol = Solution()

    assert sol.kthSmallestBS(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13
    assert sol.kthSmallestBS(matrix=[[-5]], k=1) == -5
    assert sol.kthSmallestBS(matrix=[[1, 2], [1, 3]], k=2) == 1
