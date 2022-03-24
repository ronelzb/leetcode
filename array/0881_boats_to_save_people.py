# https://leetcode.com/problems/boats-to-save-people/
# tags: #array, #greedy, #sorting, #two_pointers
#
# Solution: Sorting + Two pointers
# Sort people by weight and use two pointers to allocate them into the boats:
# * If people[start] + people[end] <= limit, it means we can insert two people into the boat and increment
# start
# * At each position decrement end to allocate at least one person into each boat
# Time complexity: O(n*log(n)), Space complexity O(1)
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end, res = 0, len(people) - 1, 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            res += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.numRescueBoats(people=[3, 2, 2, 1], limit=3))  # 3
    print(sol.numRescueBoats(people=[3, 5, 3, 4], limit=5))  # 4
