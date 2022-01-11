# https://leetcode.com/problems/fraction-to-recurring-decimal/
# tags: #google, #hash_table, #math
#
# Solution: Long division
# Use a dictionary to store a remainder and its associated index while doing the division so that
# whenever a same remainder comes up, we know there is a repeating fractional part
# PYTHON DISCLAIMER: for very small numbers out of the division Python returns the simplified number, so
# it's better to use divmod to get the integer and remainder parts when initializing
# Time complexity: O(log(n)), Space complexity O(n)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer, remainder = divmod(numerator, denominator)
        integer = sign + str(integer)
        if remainder == 0: return integer

        fraction = ""
        remainder_frac_dict = dict()
        while remainder > 0:
            if remainder in remainder_frac_dict:
                i = remainder_frac_dict[remainder]
                fraction = fraction[:i] + "(" + fraction[i:] + ")"
                break

            remainder_frac_dict[remainder] = len(fraction)
            remainder *= 10
            fraction += str(remainder // denominator)
            remainder %= denominator

        return integer + "." + fraction


if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionToDecimal(numerator=425, denominator=25))  # 17
    print(sol.fractionToDecimal(numerator=4, denominator=333))  # 0.(012)
    print(sol.fractionToDecimal(numerator=1, denominator=6))  # 0.1(6)
    print(sol.fractionToDecimal(numerator=-50, denominator=8))  # -6.25
    print(sol.fractionToDecimal(numerator=0, denominator=-5))  # 0
    print(sol.fractionToDecimal(numerator=1, denominator=214748364))
