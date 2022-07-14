# https://leetcode.com/problems/matchsticks-to-square/
# tags: #array, #backtracking, #bit_manipulation, #dp
#
# Solution 1: DFS + cache
# * Sort the matchsticks by length, then reverse check to reduce some time, because we want to
# consider the biggest one first
# * If any l1, l2, l3, l4 are greater than edge , we stop searching
# https://leetcode.com/problems/matchsticks-to-square/discuss/2274058/python-from-dfs-to-optimized-dp-using-bitmasks
# Time complexity: O(n^5) cache_entries * work_per_recursion, Space complexity O(n^5) cache_entries
from functools import cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        area = sum(matchsticks)
        if area < 4 or area % 4 != 0:
            return False

        side = area // 4
        matchsticks.sort(reverse=True)

        @cache
        def find_sides(l1, l2, l3, l4, i):
            nonlocal side

            if l1 == l2 == l3 == l4 == side:
                return True
            if i > len(matchsticks) - 1:
                return False
            if l1 > side or l2 > side or l3 > side or l4 > side:
                return False

            # Makes the cache more efficient because symmetric cases are ruled out
            x = [l1, l2, l3, l4]
            x.sort()
            l1, l2, l3, l4 = x

            return find_sides(matchsticks[i] + l1, l2, l3, l4, i + 1) \
                   or find_sides(l1, matchsticks[i] + l2, l3, l4, i + 1) \
                   or find_sides(l1, l2, matchsticks[i] + l3, l4, i + 1) \
                   or find_sides(l1, l2, l3, matchsticks[i] + l4, i + 1)

        return find_sides(0, 0, 0, 0, 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.makesquare(matchsticks=[1, 1, 2, 2, 2]))  # True
    print(sol.makesquare(matchsticks=[3, 3, 3, 3, 4]))  # False
