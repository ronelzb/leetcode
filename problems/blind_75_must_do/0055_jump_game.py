from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False

        nums[1] = max(nums[0] - 1, nums[1])
        if nums[1] == 0:
            return False

        for i in range(2, n):
            nums[i] = max(nums[i], nums[i - 1] - 1)
            if nums[i] == 0 and i < n - 1:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump(nums=[2, 3, 1, 1, 4])
    assert not sol.canJump(nums=[3, 2, 1, 0, 4])
    assert sol.canJump(nums=[[2, 0, 0]])
    assert not sol.canJump(nums=[1, 0, 2])
    assert sol.canJump(nums=[3, 0, 0, 0])
