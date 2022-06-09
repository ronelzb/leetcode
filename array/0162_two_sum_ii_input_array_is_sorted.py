# https://leetcode.com/problems/break-a-palindrome/
# tags: #array, #binary_search, #two_pointers
#
# Solution: Two pointers
# For the solution initialize two pointers: start index at 0 and end index at n - 1
# Make a while loop until both numbers in start and end index are equal to target:
# * If target is smaller, decrement j.
# * If target is larger, increment i.
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i + 1, j + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(numbers=[2, 7, 11, 15], target=9))  # [1,2]
    print(sol.twoSum(numbers=[2, 3, 4], target=6))  # [1,3]
    print(sol.twoSum(numbers=[-1, 0], target=-1))  # [1,2]
