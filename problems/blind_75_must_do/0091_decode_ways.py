# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        results_table = [0] * (n + 1)
        results_table[0] = results_table[1] = 1

        for i in range(1, n):
            if s[i] != "0":
                results_table[i + 1] += results_table[i]
            if s[i - 1] != "0" and 1 <= int(s[i - 1: i + 1]) <= 26:
                results_table[i + 1] += results_table[i - 1]

        return results_table[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings(s="226") == 3
    assert sol.numDecodings(s="12") == 2
    assert sol.numDecodings(s="0") == 0
    assert sol.numDecodings(s="06") == 0
