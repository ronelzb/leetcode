# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List


class Solution:
    # Explanation at:
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, current_sum = 0, 0
        sums = {0: 1}

        for num in nums:
            current_sum += num
            count += sums.get(current_sum - k, 0)
            sums[current_sum] = sums.get(current_sum, 0) + 1

        return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.subarraySum(nums=[1, 1, 1], k=2) == 2
