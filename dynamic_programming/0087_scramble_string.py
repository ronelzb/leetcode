# https://leetcode.com/problems/scramble-string/
# tags: #dp, #string
#
# Great explanation at:
# https://leetcode.com/problems/scramble-string/discuss/29469/C%2B%2B-solutions-w-explanation.-Both-recursive-and-Top-Down-Dynamic-Programming.
#
# Solution: 
# Time complexity: O(n^3), Space complexity O(n^3)
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def recursion(sub1: str, sub2: str) -> bool:
            if (sub1, sub2) in dp: return dp[(sub1, sub2)]
            if Counter(sub1) != Counter(sub2):
                dp[(sub1, sub2)] = False
                return False
            if len(sub1) < 4 or sub1 == sub2:
                dp[(sub1, sub2)] = True
                return True

            for i in range(1, len(sub1)):
                if recursion(sub1[:i], sub2[:i]) and recursion(sub1[i:], sub2[i:]):
                    dp[(sub1, sub2)] = True
                    return True
                if recursion(sub1[:i], sub2[-i:]) and recursion(sub1[i:], sub2[:-i]):
                    dp[(sub1, sub2)] = True
                    return True
            dp[(sub1, sub2)] = False
            return False

        dp = dict()
        return recursion(s1, s2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isScramble(s1="great", s2="rgeat"))  # True
    print(sol.isScramble(s1="abcde", s2="caebd"))  # False
    print(sol.isScramble(s1="eebaacbcbcadaaedceaaacadccd", s2="eadcaacabaddaceacbceaabeccd"))  # False
