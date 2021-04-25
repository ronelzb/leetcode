from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        r = [nums[0], max(nums[0], nums[1])]  # type: list[int]
        for i in range(2, n):
            r.append(max(r[i - 1], r[i - 2] + nums[i]))

        return r[n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
