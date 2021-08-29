# https://leetcode.com/problems/powx-n/
# tags: #divide_and_conquer, #math, #recursion
#
# Using an optimized divide-and-conquer method the function can be optimized
# to O(log(n)) by calculating power(x, y/2) only once and storing it.
#
# Time complexity: O(log(n)), Space complexity: O(log(n)) due to stack trace recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        res = self.myPow(x, int(n / 2))
        if n % 2 == 0:
            return res * res
        else:
            if n > 0:
                return x * res * res
            else:
                return (res * res) / x


if __name__ == "__main__":
    sol = Solution()

    print(sol.myPow(x=2.00000, n=10))  # 1024.0
    print(sol.myPow(x=2.10000, n=3))  # 9.261
    print(sol.myPow(x=2.00000, n=-2))  # 0.25
