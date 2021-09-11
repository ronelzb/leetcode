# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# tags: #array, #dp
#
# Explanation at:
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/92822/Detailed-explanation-for-Java-O(n2)-solution
#
# We memoize with an array of dictionaries, dp, such that dp[i][j] stores the number of arithmetic slices
# (including those with only length 2) whose constant difference is j ending at i.
# The key is basically to store all 2+-length arithmetic slices (which is helps to build up the solution
# from its sub-problems) while only adding valid 3+-length slices to the total.
#
# Then we iterate over all pairs in the array.
# Each (A[j], A[i]) is a 2-length slice with constant difference A[i] - A[j]
# that we've never encountered before, so increment dp[i][A[i] - A[j]] by 1
# (but leave the total as is, because its not length 3 or more).
#
# If there are any slices with A[i] - A[j] length that finish at index j (if A[i]-A[j] in dp[j]:),
# we 'extend' them to index i and add to the total, since any slice that terminated at index j
# would now have at least length 3 terminating at i.
#
# Time Complexity: O(n^2), Space complexity: O(n^2)
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                c1, c2 = dp[i].get(diff, 0), dp[j].get(diff, 0)
                result += c2
                dp[i][diff] = c1 + c2 + 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))  # 7
    print(sol.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))  # 16
