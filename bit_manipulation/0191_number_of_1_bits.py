# https://leetcode.com/problems/number-of-1-bits/
# tags: #bit_manipulation, #blind_75_must_do, #top_interview_questions
#
# Solution: Counter + LSB manipulation
# Traditionally we can move bit by bit until n reaches zero
# One way to optimize this is to remove the LSB (least significant bit) at each iteration which will improve performance
# Time complexity: O(1), max 5 iterations when int32, max 6 iterations when int64
# Space complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n > 0:
            n &= n - 1
            counter += 1

        return counter


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(n=17))  # 1
