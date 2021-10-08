# https://leetcode.com/problems/permutation-sequence/
# tags: #dfs, #backtracking, #math, #recursion
#
# Solution 1: Backtracking
# Time Complexity: O(n*n!), Space complexity: O(n!)
#
# Solution 2: Pattern finding
# https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
# https://leetcode.com/problems/permutation-sequence/discuss/696390/Python-Math-solution-%2B-Oneliner-both-O(n2)-expained
# Time Complexity: O(n^2), Space complexity: O(1)
from typing import List


class Solution:
    def __init__(self):
        self.counter = 0

    def getPermutation(self, n: int, k: int) -> str:
        def backtracking(s: List[str], weave: List[str]) -> List[str]:
            if not s:
                if self.counter == k:
                    return weave
                self.counter += 1
                return []

            for i in range(len(s)):
                res = backtracking(s[:i] + s[i + 1:], weave + [s[i]])
                if res: return res

        self.counter = 1
        S = [str(i) for i in range(1, n + 1)]
        return "".join(backtracking(S, []))

    def getPermutation2(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        factorial = [0] * (n + 1)

        sum = 1
        factorial[0] = 1
        for i in range(1, n + 1):
            sum *= i
            factorial[i] = sum

        k -= 1
        res = []
        for i in range(1, n + 1):
            index = k // factorial[n - i]
            res.append(str(numbers[index]))
            numbers.pop(index)
            k -= index * factorial[n - i]

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation2(n=3, k=3))  # "213"
    print(sol.getPermutation2(n=4, k=9))  # "2314"
    print(sol.getPermutation2(n=3, k=1))  # "123"
