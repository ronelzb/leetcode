# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
import heapq
from typing import List


class Solution:
    # Idea: Use heap to main smallest element first
    # The heap can be initialized using all numbers from nums1 and just the first from nums2
    # This will give us the first pair guaranteed (to maintain consistency in the while loop)
    # In the while loop pop the first element and push the current i and next j
    # Using the sum between the pair as the heap ordering criteria
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        n1, n2 = len(nums1), len(nums2)

        heap = [(nums1[i] + nums2[0], i, 0) for i in range(n1)]
        heapq.heapify(heap)

        while k > 0 and heap:
            current_sum, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])

            if j < n2 - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return pairs


if __name__ == "__main__":
    sol = Solution()

    assert sol.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [[1, 2], [1, 4], [1, 6]]
    assert sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10)  # [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2,
    # 2], [1, 3], [1, 3], [2, 3]]
