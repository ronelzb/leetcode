# https://leetcode.com/problems/majority-element/
# tags: #array, #couting, #divide_and_conquer, #hash_table, #must_do_easy_questions, #sorting
#
# Solution 1: Moore voting
# Boyer–Moore majority vote algorithm (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 2: Bit manipulation
# We will count the majority of ones or zeroes for each bit representation number starting from LSB
# Time complexity: O(log(w)*n) w=size of each num in nums, Space complexity: O(1)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter, current = 0, 0

        for num in nums:
            if counter == 0:
                current = num
                counter = 1
            elif num == current:
                counter += 1
            else:
                counter -= 1

        return current

    def majorityElement_bit(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(32):
            ones = 0
            for num in nums:
                if (1 << i) & num:
                    ones += 1

            if ones > n // 2:
                res |= (1 << i)

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(sol.majorityElement_bit(nums))  # 2
