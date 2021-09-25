# https://leetcode.com/problems/implement-strstr/
# tags: #string, #two_pointers
#
# Solution 1: Two pointers (Naive)
# For each index in m - n we try to find a match with needle
# Time Complexity: O(m*n), Space complexity: O(n)
#
# Solution 2: KMP (https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
# Use KMP pattern searching, using preprocess of the needle string
# Time complexity: O(m + n), Space complexity: O(n)
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        if n > m:
            return -1

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1

    def strStr_KMP(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        if n > m:
            return -1

        def kmp_preprocess() -> List[int]:
            i, j = 1, 0
            res = [0] * n
            while i < n:
                if needle[i] == needle[j]:
                    res[i] = j + 1
                    i += 1
                    j += 1
                elif j > 0:
                    j = res[j - 1]
                else:
                    res[i] = 0
                    i += 1
            return res

        lps = kmp_preprocess()
        i, j = 0, 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1

        return i - j if j == n else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr_KMP(haystack="hello", needle="ll"))  # 2
    print(sol.strStr_KMP(haystack="ababba", needle="abba"))  # 2
