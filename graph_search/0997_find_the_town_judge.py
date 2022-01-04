# https://leetcode.com/problems/find-the-town-judge/
# tags: #array, #graph, #hash_table
#
# Solution 1: Using dictionary
# Create one dictionary to get the counter of incoming trusts, the judge will be trusted by everyone but himself
# Create a set to the those who trusts anybody else, if somebody trusts someone else then he/she is not the judge
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: Using array
# We can use an array to get the counter of trusts, when a person trusts someone else we increase the trusted counter
# The judge must have n - 1 trusts
# Time complexity: O(n), Space complexity O(n)
from typing import List


class Solution:
    def findJudge_hashtable(self, n: int, trust: List[List[int]]) -> int:
        outgoing_trust = set()
        incoming_trust = {x: 0 for x in range(1, n + 1)}

        for x, y in trust:
            outgoing_trust.add(x)
            incoming_trust[y] += 1

        for y in incoming_trust:
            if y not in outgoing_trust and incoming_trust[y] == n - 1:
                return y
        return -1

    def findJudge_array(self, n: int, trust: List[List[int]]) -> int:
        trust_counter = [0 for _ in range(n + 1)]

        for x, y in trust:
            trust_counter[x] -= 1
            trust_counter[y] += 1

        for i in range(1, n + 1):
            if trust_counter[i] == n - 1: return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findJudge_array(n=1, trust=[]))  # 1
    print(sol.findJudge_array(n=2, trust=[[1, 2]]))  # 2
    print(sol.findJudge_array(n=3, trust=[[1, 3], [2, 3]]))  # 3
    print(sol.findJudge_array(n=3, trust=[[1, 2], [2, 3]]))  # -1
    print(sol.findJudge_array(n=3, trust=[[1, 3], [2, 3], [3, 1]]))  # -1
    print(sol.findJudge_array(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
