# https://leetcode.com/problems/k-th-symbol-in-grammar/
import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # if k is in the first half of the str recurse down a row
        # if k isn't in the first half of the str, recurse down a row and find the opposite
        # char's position in the first half
        first_half = 2 ** (n - 2)
        if k <= first_half:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 if self.kthGrammar(n - 1, k - first_half) == 0 else 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.kthGrammar(n=1, k=1) == 0
    assert sol.kthGrammar(n=2, k=2) == 1
