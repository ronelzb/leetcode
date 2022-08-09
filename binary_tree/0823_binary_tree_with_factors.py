# https://leetcode.com/problems/binary-trees-with-factors/
# tags: #array, #dp, #hash_table
#
# Solution: Dynamic Programming
# * Sort the array in ascending order
# * Initialize a dictionary with each num in arr with 1 as value
# * Traverse each number in the array, having num % arr[j] == 0 (where j < i) as the left child of the current node
#   and arr[i] // arr[j] which would be the right child of the current node
#   Then, we can get all the permutations available to add to this node
# * Return the sum of the values in the dictionary
# Time complexity: O(n), Space complexity O(1) each stack will never grow beyond 3 elements
from collections import Counter
from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = Counter(arr)

        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0 and num // arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]
                    dp[num] %= self.MOD

        return sum(dp.values()) % self.MOD


if __name__ == '__main__':
    sol = Solution()
    print(sol.numFactoredBinaryTrees(arr=[2, 4]))  # 3
    print(sol.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))  # 7
