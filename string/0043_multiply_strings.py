# https://leetcode.com/problems/multiply-strings/
# tags: #google, #math, #simulation, #string
#
# Graphical explanation at:
# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
#
# Solution: Two pass
# First pass start from right to left, perform multiplication on every pair of digits, and add them together
# We pre-allocate our result summing multiplication result into the current index (i + j + 1), this will give
# use the result and sum the carry to the next position (i + j) at the same time.
# In the second pass bypass the non-significant zeroes to the left.
# Time Complexity: O(m*n), Space complexity: O(m + n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mult = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                mult += result[i + j + 1]

                result[i + j] += mult // 10
                result[i + j + 1] = mult % 10

        i = 0
        while i < m + n and result[i] == 0:
            i += 1

        return "".join(map(str, result[i:])) if i < m + n else "0"


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply(num1="123", num2="45"))  # "5535"
    print(sol.multiply(num1="9", num2="9"))  # "81"
