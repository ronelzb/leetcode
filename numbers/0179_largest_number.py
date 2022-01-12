# https://leetcode.com/problems/largest-number/
# tags: #greedy, #microsoft, #sorting, #string
#
# Solution: Sort custom comparison
# Define a function that compares two strings: a, b. Considering if a + b > b + a
# Eg.: a="2",b="11" a is bigger than b because "211" >"112"
# Time complexity: O(n+k*n*log(n)) k=cost of string comparison, Space complexity O(n)
import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(a, b): return 1 if a + b > b + a else - 1 if a + b < b + a else 0

        return str(int("".join(sorted(map(str, nums),
                                      key=functools.cmp_to_key(comparator),
                                      reverse=True))))


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber(nums=[10, 2]))  # "210"
    print(sol.largestNumber(nums=[3, 30, 34, 5, 9]))  # "9534330"
    print(sol.largestNumber(nums=[0, 0]))  # "0"
