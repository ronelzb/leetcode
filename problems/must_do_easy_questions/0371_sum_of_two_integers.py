# https://leetcode.com/problems/sum-of-two-integers/submissions/
# tags: #math, #bit_manipulation
#
# Solution: Bit manipulation
# Time complexity: O(1) It will loop at most 32 times, Space complexity: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def _sum(x: int, y: int):
            while y:
                carry = x & y
                x ^= y
                y = carry << 1

            return x

        if a * b < 0:
            if -a == b:
                return 0
            if a > 0:
                return self.getSum(b, a)
            if -a < b:
                return -_sum(-a, -b)

        return _sum(a, b)


if __name__ == "__main__":
    sol = Solution()
    assert sol.getSum(1, 2) == 3
    assert sol.getSum(2, 3) == 5
    assert sol.getSum(-14, 16) == 2
