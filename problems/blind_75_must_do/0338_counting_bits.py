# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    # O(n log(n))
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            num = i

            count_ones = 0
            while num:
                count_ones += 1
                num &= num - 1
            ans[i] = count_ones

        return ans

    # O(n)
    # Explanation: https://leetcode.com/problems/counting-bits/discuss/657594/Python-3-today's-one-liner
    # Consider a number n with x bits.
    # Then 2 * n also has x bits (it's the same number shifted to the left by 1), and 2 * n + 1 has x + 1 bits.
    def countBits_optimized(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # assert sol.countBits(n=5) == [0, 1, 1, 2, 1, 2]
    print(sol.countBits_optimized(n=16))  # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
