# https://leetcode.com/problems/reverse-bits/
# tags: #blind_75_must_do, #top_interview_questions
#
# Solution 1: Bit manipulation
# Traverse all 32 integer bits, if we find that a bit is present allocate it reverse in the result (1 << (31 - i))
# Time complexity: O(1), Space complexity: O(1)
#
# Solution 2: Python built-in
# Use Python bin method to convert the number into a binary string
# Return the reversed representation of the number in binary
# Time complexity: O(1), Space complexity: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n & 1:
                result += 1 << (31 - i)
            n >>= 1

        return result

    def reverseBits_string(self, n: int) -> int:
        bin_num = bin(n)[2:].zfill(32)
        return int(bin_num[::-1], 2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(n=43261596))
