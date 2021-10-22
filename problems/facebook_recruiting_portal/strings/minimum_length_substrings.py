# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2237975393164055&c=896138004629128&ppid=454615229006519&practice_plan=0
# LeetCode 76. Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/
# My solution: https://github.com/ronelzb/leetcode/tree/master/string/0076_minimum_window_substring.py
# Time Complexity: O(m + n), Space complexity: O(n)
import sys
from collections import Counter


class Solution:
    def min_length_substring(self, s: str, t: str) -> 5:
        t_counter = Counter(t)
        n = len(t)

        start, min_length = 0, sys.maxsize
        for i, c in enumerate(s):
            if c in t_counter:
                if t_counter[c] > 0:
                    n -= 1
                t_counter[c] -= 1

            while n == 0:
                if i - start < min_length:
                    min_length = i - start
                if s[start] in t_counter:
                    t_counter[s[start]] += 1
                    if t_counter[s[start]] > 0:
                        n += 1

                start += 1

        return min_length + 1 if min_length < sys.maxsize else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.min_length_substring(s="dcbefebce", t="fd"))  # 5
    print(sol.min_length_substring(s="bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", t="cbccfafebccdccebdd"))  # -1
