# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# tags: #array, #google, #greedy, #one_pass_counting #set_union
#
# Solution #1:
# My first intuition was to start with tops[0] and bottoms[0] as possible candidates
# But then I realize we can do a one-pass count to get both arrays count and an additional pass
# to get those indexes with the same numbers
# The solution suggests: Iterate for each number in the domino which satisfies the condition
# tops_count[num] + bottoms[count] - same[count] = n and just get the min value
#
# Time complexity: O(3 * n + 6) => O(n), Space complexity: O(3 * 6) => O(1)
#
#
# Solution #2:
# Another solution is a greedy approach
# As the first solutions we need to count each occurrence in tops and bottoms to find the min swaps
# but this time we'll do it manually: count the occurrences from the first tops and,
# if the result is -1 search first bottoms
#
# Time complexity: O(2 * n) => O(n), Space complexity(1)
from collections import Counter
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        same_count, tops_count, bottoms_count = Counter(), Counter(tops), Counter(bottoms)

        for top, bottom in zip(tops, bottoms):
            if top == bottom:
                same_count[top] += 1

        for i in range(1, 7):
            if tops_count[i] + bottoms_count[i] - same_count[i] == len(tops):
                return min(tops_count[i], bottoms_count[i]) - same_count[i]

        return -1

    def minDominoRotationsGreedy(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def check_rotations(x):
            rotations_a, rotations_b = 0, 0

            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return - 1
                if tops[i] == x and bottoms[i] == x:
                    continue

                if tops[i] == x:
                    rotations_a += 1
                if bottoms[i] == x:
                    rotations_b += 1

            return min(rotations_a, rotations_b)

        rotations = check_rotations(tops[0])
        if rotations == -1:
            rotations = check_rotations(bottoms[0])

        return rotations


if __name__ == "__main__":
    sol = Solution()

    print(sol.minDominoRotationsGreedy(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))  # 2
    print(sol.minDominoRotationsGreedy(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))  # -1
