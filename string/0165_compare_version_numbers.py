# https://leetcode.com/problems/compare-version-numbers/
# tags: #string, #two_pointers
#
# Solution: Two Pointers
# 1. Split each string to an array of numbers
# 2. Complement the shorter array with zero elements to equalize both arrays length
# 3. Compare s1 and s2 as lists.
# Time complexity: O(m+n), Space complexity O(m+n)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = [int(s) for s in version1.split(".")]
        s2 = [int(s) for s in version2.split(".")]

        l1, l2 = len(s1), len(s2)
        if l1 > l2: s2 += [0] * (l1 - l2)
        else: s1 += [0] * (l2 - l1)

        if s1 > s2: return 1
        elif s1 < s2: return -1
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion(version1="1.01", version2="1.001"))  # 0
    print(sol.compareVersion(version1="1.0", version2="1.0.0"))  # 0
    print(sol.compareVersion(version1="0.1", version2="1.1"))  # -1
