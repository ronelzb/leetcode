# https://leetcode.com/problems/k-th-symbol-in-grammar/
# tags: #bit_manipulation, #math, #recursion
#
# Solution 1: Evaluate even and odd values
# if k is in the first half of the str recurse down a row
# if k isn't in the first half of the str, recurse down a row and find the opposite
# char's position in the first half
# Time complexity: O(log(k)), Space complexity: O(log(k))
#
# Solution 2: Bit manipulation
# Turn this problem to count bits of 1.
# We can observe that the answer depend on whether the number of 1-bit in the binary number K - 1 is odd or even.
# Time complexity: O(log(k)), Space complexity: O(log(k))
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        first_half = 2 ** (n - 2)
        if k <= first_half:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 if self.kthGrammar(n - 1, k - first_half) == 0 else 0

    def kthGrammar_bit(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1


if __name__ == "__main__":
    sol = Solution()

    assert sol.kthGrammar(n=1, k=1) == 0
    assert sol.kthGrammar(n=2, k=2) == 1
