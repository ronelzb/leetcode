# https://leetcode.com/problems/last-stone-weight/
# tags: #array, #heap
#
# Solution: Heap
# Add all negated elements into a heap, this will provide us with a max-heap required by the problem
# Pop out the two biggest elements, insert the remaining back if it's greater than zero until
# there are no more than two elements in the list
# Time complexity: O(n*log(n)), Space complexity O(n)
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            remaining = heapq.heappop(stones) - heapq.heappop(stones)
            if remaining != 0:
                heapq.heappush(stones, remaining)

        return -stones[0] if len(stones) > 0 else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))  # 1
