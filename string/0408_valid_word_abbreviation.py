# https://leetcode.com/problems/valid-word-abbreviation/
# tags: #facebook, #string, #two_pointers
#
# Solution 1: Two pointers
# Time complexity: O(m), Space complexity O(1)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        p, q = 0, 0

        while p < m and q < n:
            if abbr[q].isalpha():
                if word[p] != abbr[q]:
                    return False
                p += 1
                q += 1
            else:
                if abbr[q] == "0":
                    return False

                length = 0
                while q < n and abbr[q].isdigit():
                    length = length * 10 + int(abbr[q])
                    q += 1

                if p + length > m:
                    return False
                p += length

        return p == m and q == n


if __name__ == '__main__':
    sol = Solution()
    print(sol.validWordAbbreviation(word="internationalization", abbr="i12iz4n"))  # True
    print(sol.validWordAbbreviation(word="apple", abbr="a2e"))  # False
    print(sol.validWordAbbreviation(word="apple", abbr="a4"))  # True
    print(sol.validWordAbbreviation(word="hi", abbr="hi1"))  # False
