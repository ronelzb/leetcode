# https://leetcode.com/problems/reverse-bits/
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
