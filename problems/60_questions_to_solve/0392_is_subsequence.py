# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n_s, n_t = len(s), len(t)
        if n_s == 0:
            return True
        if n_s > n_t:
            return False

        index_s = -1
        for c in t:
            if c == s[index_s + 1]:
                index_s += 1
                if index_s == n_s - 1:
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.isSubsequence(s="abc", t="ahbgdc")
    assert not sol.isSubsequence(s="axc", t="ahbgdc")
