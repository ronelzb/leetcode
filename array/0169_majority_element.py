# https://leetcode.com/problems/majority-element/
# tags: #array, #couting, #divide_and_conquer, #hash_table, #must_do_easy_questions, #sorting
#
# Solution: Moore voting
# Boyer–Moore majority vote algorithm (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
# Time complexity: O(n), Space complexity: O(1)
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


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(sol.majorityElement(nums))
