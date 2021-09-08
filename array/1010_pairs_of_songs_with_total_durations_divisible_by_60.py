# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# tags: #array, #counting, #hash_table
#
# Search for the complement. Any multiple of 60 will complement itself. Since he maps multiple of 60 -> 0, other is 0.
# (t + other_song) % 60 == 0 => other_song = (60 - t % 60) % 60 => other_song = -t % 60
# After that, the rest is very similar to Two Sum problem
#
# Time Complexity: O(n), Space complexity: O(60) => O(1)
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums_to_idx = defaultdict(int)
        songs_divisible = 0

        for t in time:
            other_song = -t % 60
            songs_divisible += nums_to_idx[other_song]
            nums_to_idx[t % 60] += 1

        return songs_divisible


if __name__ == "__main__":
    sol = Solution()
    print(sol.numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]))  # 3
