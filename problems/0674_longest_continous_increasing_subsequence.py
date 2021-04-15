from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        max_count, count = 1, 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        return max_count


if __name__ == "__main__":
    sol = Solution()

    assert sol.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
    assert sol.findLengthOfLCIS([2, 2, 2]) == 1
    assert sol.findLengthOfLCIS([]) == 0
    assert sol.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]) == 4