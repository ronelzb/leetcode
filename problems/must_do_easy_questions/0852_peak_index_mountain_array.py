from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = left = 0
        right = len(arr) - 1

        while not peak:
            middle = (left + right) // 2

            if arr[middle - 1] < arr[middle] > arr[middle + 1]:
                peak = middle
            elif arr[middle - 1] < arr[middle]:
                left = middle
            else:
                right = middle

        return peak


if __name__ == "__main__":
    sol = Solution()
    assert sol.peakIndexInMountainArray([0, 1, 0]) == 1
    assert sol.peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert sol.peakIndexInMountainArray([0, 10, 5, 2]) == 1
    assert sol.peakIndexInMountainArray([3, 4, 5, 1]) == 2
    assert sol.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]) == 2
