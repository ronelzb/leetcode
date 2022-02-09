# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# tags: #array, #binary_search, #hash_table, #sorting, #two_pointers
#
# Solution 1: Counter
# Count the elements in nums:
# * If k > 0, check if i + k exist.
# * If k == 0, check if count[i] > 1
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: Sorting + Two pointers
# 2-sum Variant, sort the array and move the pointers:
# * Move end if nums[start] + k > nums[end] or start == end
# * Move start if nums[start] + k < nums[end]
# * Else means nums[start] + k == nums[end] then increase pairs found and move start while a new num is found
# Then move end forward to start
# Time complexity: O(n*log(n)), Space complexity O(1)
from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        pairs = 0

        for num in counter:
            if (k > 0 and num + k in counter) or (k == 0 and counter[num] > 1):
                pairs += 1

        return pairs

    def findPairs_sortandtwopointers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        start, end, pairs = 0, 1, 0

        while start < n and end < n:
            if start == end or nums[start] + k > nums[end]:
                end += 1
            elif nums[start] + k < nums[end]:
                start += 1
            else:
                start += 1
                pairs += 1

                while start < n and nums[start] == nums[start - 1]:
                    start += 1
                end = max(end + 1, start + 1)

        return pairs


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPairs_sortandtwopointers(nums=[3, 1, 4, 1, 5], k=2))  # 2
    print(sol.findPairs_sortandtwopointers(nums=[1, 2, 3, 4, 5], k=1))  # 4
    print(sol.findPairs_sortandtwopointers(nums=[1, 3, 1, 5, 4], k=0))  # 1
