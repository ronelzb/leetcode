# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter
from typing import List


class Solution:
    # most_common = O(n log(n)), therefore time complexity = O(n log(n))
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [c[0] for c in Counter(nums).most_common(k)]

    # follow up: Use min-heap to get the largest k elements
    # Using heap is best suited for the interview and we're being less lazy than the first solution :)
    def topKFrequent_optimized(self, nums: List[int], k: int) -> List[int]:
        h = heapq.nlargest(k, [(freq, key) for key, freq in Counter(nums).items()])
        return [key for freq, key in h]


if __name__ == "__main__":
    sol = Solution()

    assert sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2] or [2, 1]
    assert sol.topKFrequent_optimized(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2] or [2, 1]
