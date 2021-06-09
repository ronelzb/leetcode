# https://leetcode.com/problems/string-to-integer-atoi/
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        m = re.match(r'\s*([+|-]?\d+)', s)

        return min(max(int(m.group()), -2 ** 31), 2 ** 31 - 1) if m else 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.myAtoi(s="4193 with words") == 4193
    assert sol.myAtoi(s="words and 987") == 0
    assert sol.myAtoi(s="-91283472332") == -2147483648
