# https://leetcode.com/problems/wiggle-sort-ii/
# tags: #array, #divide_and_conquer, #sorting, #quickselect
#
# Solution: Sorting
# * Sort the input array and instantiate an auxiliary array
# * Iterate from the back of the array (descending) filling up the auxiliary array starting from index 1.
# * In the auxiliary, we'll jump 2 spaces after every assignation. When reaching the end, reset the index back to 0
# Time complexity: O(n*log(n)), Space complexity O(n)
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2: return
        nums.sort()
        aux = [0] * n
        j = 1

        for i in range(n - 1, -1, -1):
            aux[j] = nums[i]
            j += 2
            if j >= n: j = 0

        for i in range(n):
            nums[i] = aux[i]


if __name__ == "__main__":
    sol = Solution()
    test_nums = [1, 5, 1, 1, 6, 4]
    sol.wiggleSort(test_nums)
    print(test_nums)  # [1,6,1,5,1,4]

    test_nums = [1, 3, 2, 2, 3, 1]
    sol.wiggleSort(test_nums)
    print(test_nums)  # [2,3,1,3,1,2]
