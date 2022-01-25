# https://leetcode.com/problems/valid-mountain-array/
# tags: #array
#
# Solution: One pass
# Try to get to the end of the array with the pointer i if the values increases then decreases
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[0] >= arr[1]: return False
        i = 1

        while i < n and arr[i] > arr[i - 1]: i += 1
        if i == n: return False
        while i < n and arr[i] < arr[i - 1]: i += 1

        return i == n


if __name__ == "__main__":
    sol = Solution()
    print(sol.validMountainArray(arr=[3, 5, 5]))  # False
    print(sol.validMountainArray(arr=[0, 3, 2, 1]))  # True
    print(sol.validMountainArray(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # False
