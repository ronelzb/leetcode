# https://leetcode.com/problems/contiguous-array/
# tags: #array, #hash_table, #prefix_sum
#
# Solution: Dictionary + count
# Similar idea to problem 121. Best Time to Buy and Sell Stock
# Create a variable count initially equals 0 and traverse through nums.
# Every time we meet a 0, we decrease count by 1, and increase count by 1 when we meet 1
# To find the maximum length, we need a dict to store the value of count (as the key)
# and its associated index (as the value).
# We only need to save a count value and its index at the first time, when the same count values appear again,
# we use the new index subtracting the old index to calculate the length of a subarray
#
# Why do we start the dictionary at {0, -1}?
# Taking this problem to a plot, the keys would be y and the values x, this init corresponds to [-1, 0].
# Time complexity: O(n), Space complexity O(n)
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_dict = {0: -1}
        max_length, count = 0, 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else - 1

            if count in map_dict:
                max_length = max(max_length, i - map_dict[count])
            else:
                map_dict[count] = i

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength(nums=[0, 1, 0, 1, 0, 1]))  # 6
    print(sol.findMaxLength(nums=[0, 0, 0, 0, 1, 1]))  # 4
    print(sol.findMaxLength(nums=[0, 0, 1, 0, 0, 0, 1, 1]))  # 6
