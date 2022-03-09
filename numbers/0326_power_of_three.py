# https://leetcode.com/problems/power-of-three/
# tags: #math, #recursion, #top_interview_questions
#
# Solution: Loop
# Divide the number until is divisible by 3, or it goes down to 1
# Time complexity: O(log3(n)), Space complexity O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        while n > 1:
            if n % 3 != 0: return False
            n //= 3

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(n=27))  # True
    print(sol.isPowerOfThree(n=2))  # False
    print(sol.isPowerOfThree(n=0))  # False
