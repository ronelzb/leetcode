# https://leetcode.com/problems/4sum-ii/
from collections import defaultdict
from typing import List


class Solution:
    # Idea: a + b + c + d == 0 => a + b == - c - d
    # Time complexity: O(n**2), space: O(a + b)
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_ab = defaultdict(int)
        count = 0

        for i in nums1:
            for j in nums2:
                sum_ab[i + j] += 1

        for i in nums3:
            for j in nums4:
                count += sum_ab[-(i + j)]

        return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2
