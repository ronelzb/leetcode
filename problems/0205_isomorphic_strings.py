class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = dict()

        for i in range(len(s)):
            if s[i] in pairs:
                if pairs[s[i]] != t[i]:
                    return False
            else:
                if t[i] in pairs.values():
                    return False
                pairs[s[i]] = t[i]

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic(s="egg", t="add")
    assert not sol.isIsomorphic(s="foo", t="bar")
    assert sol.isIsomorphic(s="paper", t="title")
    assert not sol.isIsomorphic(s="bbbaaaba", t="aaabbbba")
