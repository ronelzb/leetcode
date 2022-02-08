# https://leetcode.com/problems/largest-number/
# tags: #math, #number_theory, #simulation
#
# Solution 1: Iteration
# Convert num into digits, sum them together and then repeat the process until the num becomes less than 10.
# Time complexity: O(ceil(log10(n))^2) => O(log(n)^2), Space complexity O(1)
#
# Solution 2: Recursion
# Recursive implementation from solution 1
# Time complexity: O(log(n)^2), Space complexity O(log(n))
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            new_num = 0
            while num > 0:
                new_num += num % 10
                num //= 10

            num = new_num

        return num

    def addDigits_recursion(self, num: int) -> int:
        if num < 10:
            return num

        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10

        return self.addDigits_recursion(sum_num)


if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits_recursion(num=38))  # "2"
