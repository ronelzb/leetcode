# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ones, i = 0, 0

        while i < 32 and n > 0:
            if n & 1:
                count_ones += 1
            i += 1
            n >>= 1
        return count_ones


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(n=17))
