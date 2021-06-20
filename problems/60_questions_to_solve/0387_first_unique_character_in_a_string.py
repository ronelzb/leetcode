# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.firstUniqChar(s="leetcode") == 0
    assert sol.firstUniqChar(s="loveleetcode") == 2
    assert sol.firstUniqChar(s="aabb") == -1
