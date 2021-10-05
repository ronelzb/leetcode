# https://leetcode.com/problems/longest-consecutive-sequence/
# array, #hash_table, #union_find
#
# Solution 2: One pass
# Sort the array and traverse through the array checking the longest streak at each index
# Time complexity: O(n*log(n)), Space complexity: O(1)
#
# Solution 2: Dictionary sequence building
# Keep track of the sequence length and store that in the boundary points of the sequence.
# Time complexity: O(n), Space complexity: O(n)
from typing import List


class Solution:
    def longestConsecutive_onePass(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        nums.sort()
        current, longest = 1, 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1

        return max(longest, current)

    def longestConsecutive_dict(self, nums: List[int]) -> int:
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
