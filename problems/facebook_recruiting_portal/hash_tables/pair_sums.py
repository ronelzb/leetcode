# Time Complexity: O(n), Space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def numberOfWays(self, arr: List[int], k: int):
        counter = defaultdict(int)
        pair_sums = 0
        for i, num in enumerate(arr):
            if num > k: continue
            remaining = k - num

            if remaining in counter:
                pair_sums += counter[remaining]

            counter[num] += 1

        return pair_sums


if __name__ == "__main__":
    sol = Solution()
    assert sol.numberOfWays([1, 2, 3, 4, 3], 6) == 2
    assert sol.numberOfWays([1, 5, 3, 3, 3], 6) == 4
