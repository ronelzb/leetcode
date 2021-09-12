# https://leetcode.com/problems/reverse-integer/
# tags: #math
#
# Solution 1: Using modulo
# Time Complexity: O(k) k=integer length, Space complexity: O(k)
#
# Solution 2: Int -> str -> int
# Time Complexity: O(k), Space complexity: O(k)
#
# Solution 3: Recursion
# Time complexity: O(k), Space complexity: O(k) k=recursion stack trace for each digit in number
class Solution:
    def reverse_modulo(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        if is_negative:
            result = -result
        return result if -2147483649 < result < 2147483648 else 0

    def reverse_str(self, x: int) -> int:
        negative_flag = 1
        if x < 0:
            negative_flag = -1
            str_x = str(x)[1:]
        else:
            str_x = str(x)

        x = int(str_x[::-1])
        return x * negative_flag if x <= pow(2, 31) else 0

    def reverse_recursion(self, x: int, rev: int = 0, negative_flag: int = 0) -> int:
        if abs(rev) > pow(2, 31):
            return 0
        if negative_flag == 0:
            negative_flag = -1 if x < 0 else 1
            x = abs(x)
        if x // 10 == 0:
            return negative_flag * (rev + x)
        return self.reverse_recursion(x // 10, (rev + (x % 10)) * 10, negative_flag)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse_recursion(x=123))  # 321
    print(sol.reverse_recursion(x=-456))  # -654
    print(sol.reverse_recursion(x=1534236469))  # 0
