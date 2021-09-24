# https://leetcode.com/problems/integer-to-roman/
# tags: #hash_table, #math, #string
#
# Solution: Dictionary - numbers to roman
# Make an equivalence table or dictionary with each conversion and reverse iterate until number == 0
# Time Complexity: O(3*(n of digits) + 1) => O(log(n) base 10), Space complexity: O(log(n) base 10)
class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_symbol = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"),
                           (10, "X"), (40, "XL"), (50, "L"), (90, "XC"),
                           (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]
        n = len(value_to_symbol)
        i = n - 1
        roman = ""

        while num > 0:
            while value_to_symbol[i][0] > num:
                i -= 1

            roman += value_to_symbol[i][1]
            num -= value_to_symbol[i][0]

        return roman


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(num=58))  # "LVIII"
    print(sol.intToRoman(num=1994))  # "MCMXCIV"
