# https://leetcode.com/problems/jump-game/
# tags: #array, #dp, #greedy
#
# Solution: Dynamic Programming
# Keep track of the furthest reachable index (as the problem implies: maximal jumps where you can hit
# a range of targets instead of singular jumps where you can only hit one target).
# We iterate over each index, and if we ever encounter an index that is not reachable,
# we abort and return false. By the end, we will have iterated to the last index.
# If the loop finishes, then the last index is reachable.
# Time complexity: O(n), Space complexity: O(1) in-place
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False

        # This case improves overall time by a lot!
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
