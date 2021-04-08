from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = None
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if index is None:
                    index = i
                else:
                    return False

        if index is None or index == 0 or index == n - 2 \
                or nums[index - 1] <= nums[index + 1] or nums[index] <= nums[index + 2]:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.checkPossibility([4, 2, 3])
    assert not sol.checkPossibility([4, 2, 1])
    assert not sol.checkPossibility([3, 4, 2, 3])
