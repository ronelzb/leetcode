# https://leetcode.com/problems/long-pressed-name/
# tags: #greedy, #queue, #stack, #string
#
# Solution: Greedy
# * Create each permutation of covers for each character in stamp
# * Scan through the target while:
#    * If we have find part of target that is in stamp_covers, we store the index and cover the target with a wildcard.
#    * If we cannot find any part then we cannot obtain the target from the current stamp.
# * After the loop checks, target will be wildcard * len(target).
# We just need to reverse the result and return it
# Time complexity: O(n*(n-m)), Space complexity: O(n*(n-m))
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        res = []
        stamp_covers = set()

        for i in range(m):
            for j in range(m - i):
                stamp_covers.add("*" * i + stamp[i:m - j] + "*" * j)

        p = n - m + 1
        end = "*" * n

        while target != end:
            found = False
            for i in reversed(range(p)):
                if target[i: i + m] in stamp_covers:
                    target = target[:i] + "*" * m + target[i + m:]
                    res.append(i)
                    found = True

            if not found:
                return []

        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.movesToStamp(stamp="abc", target="ababc"))  # [0, 2]
    print(sol.movesToStamp(stamp="abca", target="aabcaca"))  # [3, 0, 1]
    print(sol.movesToStamp(target="aabccbabc", stamp="abc"))  # [4, 0, 6, 2, 1]
