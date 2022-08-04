# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends
# tags: #array, #google, #union_find
#
# Solution: Union-Find
# Initially, each person belongs to their own set
# Update the set (relationship) of each person in merged_set to point to the merged_set
# Time complexity: O(n*log(n)), Space complexity: O(n+m) m=logs
from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        person_relationships = {person: {person} for person in range(n)}

        for timestamp, person1, person2 in sorted(logs):
            merged_set = person_relationships[person1] | person_relationships[person2]

            for person in merged_set:
                person_relationships[person] = merged_set

            if len(merged_set) == n:
                return timestamp

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.earliestAcq(
        logs=[[20190101, 0, 1],
              [20190104, 3, 4],
              [20190107, 2, 3],
              [20190211, 1, 5],
              [20190224, 2, 4],
              [20190301, 0, 3],
              [20190312, 1, 2],
              [20190322, 4, 5]], n=6))  # 20190301

    print(sol.earliestAcq(logs=[[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], n=4))  # 3
