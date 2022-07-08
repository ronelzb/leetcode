# https://leetcode.com/problems/gas-station/
# tags: #array, #dp
#
# Solution: Dynamic Programming
# https://leetcode.com/problems/paint-house-iii/discuss/2254715/Java-or-2-methods-or-Explained
# Time complexity: O(n), Space complexity O(1)
import sys
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}

        def dfs(i: int, k: int, t: int) -> int:
            if t < 0 or t > m - i:
                return sys.maxsize
            if i == m:
                return 0 if t == 0 else sys.maxsize
            if (i, k, t) not in memo:
                if houses[i]:
                    memo[(i, k, t)] = dfs(i + 1, houses[i], t-(houses[i] != k))
                else:
                    memo[(i, k, t)] = min(cost[i][j - 1] + dfs(i + 1, j, t-(j != k)) for j in range(1, n + 1))

            return memo[(i, k, t)]

        ans = dfs(0, 0, target)
        return ans if ans < sys.maxsize else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost(
        houses=[0, 0, 0, 0, 0],
        cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
        m=5, n=2, target=3))  # 9
