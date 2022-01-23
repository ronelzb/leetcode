# https://leetcode.com/problems/sequential-digits/
# tags: #enumeration
#
# Solution 1: Generator
# Generate numbers using the required sequence and check if it's between the given bounds
# Time complexity: O(1), Space complexity O(1)
#
# Solution 1: Queue
# At each step we are going to extract number and put this number incremented to the end of the queue
# Time complexity: O(1), Space complexity O(1)
from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def next_sequential(num: int) -> iter:
            num = next = num
            while num <= high and next < 10:
                if num >= low:
                    yield num
                next += 1
                num = num * 10 + next

        return sorted([num for digit in range(1, 9) for num in next_sequential(digit)])

    def sequentialDigits_queue(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 9))

        while queue:
            num = queue.popleft()
            if low <= num <= high:
                res.append(num)
            previous = num % 10
            if previous < 9: queue.append(num * 10 + previous + 1)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.sequentialDigits_queue(low=100, high=300))  # [123,234]
    print(sol.sequentialDigits_queue(low=1000, high=13000))  # [1234,2345,3456,4567,5678,6789,12345]
