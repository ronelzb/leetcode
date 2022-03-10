# https://leetcode.com/problems/factorial-trailing-zeroes/
# tags: #must_do_easy_questions, #top_interview_questions
#
# Solution: Factorial products
# 10 is the product of 2 and 5. In n!, we need to know how many 2 and 5,
# and the number of zeros is the minimum of the number of 2 and the number of 5.
# Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
# We return the count of 5's: return n/5 + n/25 + n/125 + n/625 + n/3125+...;
# Time complexity: O(log5(n)), Space complexity: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0

        while n > 0:
            n //= 5
            result += n

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(5))
