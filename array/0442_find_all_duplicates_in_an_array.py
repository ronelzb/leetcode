# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# tags: #array, #hash_table
#
# Solution 2: Re arrange numbers
# https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
# Time Complexity: O(n), Space complexity: O(1)
#
# Solution 1: Hash numbers (Turn each number negative)
# When a number in index is found, flip the number at position index-1 to negative
# If the number at position index-1 is already negative, index is the number that occurs twice.
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def findDuplicates_rearrange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [nums[i] for i in range(n) if i != nums[i] - 1]

    def findDuplicates_hash(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            k = abs(nums[i]) - 1
            if nums[k] < 0:
                res.append(abs(k + 1))
            nums[k] = -nums[k]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates_hash(nums=[4, 3, 2, 7, 8, 2, 3, 1]))  # [2,3]
