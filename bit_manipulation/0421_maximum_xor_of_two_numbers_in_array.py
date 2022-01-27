# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# tags:
#
# Solution: Bit manipulation
# TwoSum variation, great explanation at:
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/166211/Python-O(n)-solution-for-dummies-like-me-easy-commented-solution-with-explanation
# Time complexity: O(n) some people call it O(32), Space complexity O(n)
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(32, -1, -1):
            mask |= 1 << i
            found = set([num & mask for num in nums])
            start = res | 1 << i

            for prefix in found:
                if start ^ prefix in found:
                    res = start
                    break

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))  # 28
    print(sol.findMaximumXOR(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))  # 127
