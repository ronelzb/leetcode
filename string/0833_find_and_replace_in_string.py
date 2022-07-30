# https://leetcode.com/problems/find-and-replace-in-string/
# tags: #array, #sorting, #string
#
# Solution: String replacements
# Indices/sources/targets have the same length, so we can use zip in this case
# When we find a match in the string we replace the first match index with the target
# And empty the rest of the indices (note that we don't remove the indices to keep the initial length)
# Time complexity: O(n) + O(k*x) k=len(indices) x=max(len(source)), Space complexity: O(n)
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = list(s)
        for index, source, target in zip(indices, sources, targets):
            if s[index: index + len(source)] == source:
                res[index] = target
                for i in range(index + 1, index + len(source)):
                    res[i] = ""

        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findReplaceString(s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))  # "eeebffff"
    print(sol.findReplaceString(s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))  # "eeecd"
