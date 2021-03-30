from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram(s="anagram", t="nagaram")
    assert not sol.isAnagram(s="rat", t="car")
