# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        permutations = [0] * n
        permutations[0] = 1
        permutations[1] = 2

        for i in range(2, n):
            permutations[i] = permutations[i - 1] + permutations[i - 2]

        return permutations[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(n=4) == 5
