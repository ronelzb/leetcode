# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        while nums_set:
            pivot = nums_set.pop()
            current_sequence = 1
            upper_bound, lower_bound = pivot + 1, pivot - 1

            while upper_bound in nums_set:
                nums_set.remove(upper_bound)
                upper_bound += 1
                current_sequence += 1

            while lower_bound in nums_set:
                nums_set.remove(lower_bound)
                lower_bound -= 1
                current_sequence += 1

            longest_sequence = max(current_sequence, longest_sequence)

        return longest_sequence


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
    # assert sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
