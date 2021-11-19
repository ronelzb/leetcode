# https://leetcode.com/problems/hamming-distance/
# tags: #bit_manipulation
#
# Solution: Bit count
# Hamming distance is a metric for comparing two binary data strings.
# In order to calculate the Hamming distance between two strings, and, we perform their XOR operation, (a ^ b),
# and then count the total number of 1s in the resultant string.
# Time complexity: O(n), Space complexity O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(x=1, y=4))  # 2
