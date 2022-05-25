# https://leetcode.com/problems/russian-doll-envelopes/
# tags: #binary_search, #dp, #sorting
#
# Solution: Sorting + Dynamic Programming
# We will sort the first parameter in ascending and the 2nd parameter in descending so that we get width part sorted.
# Height part is kept descending so that for same width we don't insert smaller width into larger width
# For each envelope, it can occur the following:
# * if height and width is bigger than the last envelope in the pile, create a new pile
# * if envelope is smaller than top envelope of pile, update top envelope of pile
# * if height and width is bigger than the envelope in our piles, create a new pile
# Time complexity: O(n*log(n)), Space complexity: O(n)
from typing import List


class Solution:
    def maxEnvelopes_sort(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        piles = []

        for env in envelopes:
            if piles and piles[-1][0] < env[0] and piles[-1][1] < env[1]:
                piles.append(env)
                continue

            for i in range(len(piles)):
                if piles[i][1] >= env[1]:
                    piles[i] = env
                    break
            else:
                piles.append(env)

        return len(piles)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxEnvelopes_sort(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))  # 3
    print(sol.maxEnvelopes_sort(envelopes=[[1, 1], [1, 1], [1, 1]]))  # 1
