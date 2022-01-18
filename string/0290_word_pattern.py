# https://leetcode.com/problems/word-pattern/
# tags: #hash_table, #string
#
# Solution: 2 dictionaries
# Split the input s by empty spaces to make the equivalence pattern/sub_s
# Iterate one by one the elements from pattern and words keeping two dictionaries:
# * One is for word -> letter
# * And another for letter -> word.
# The important part here is the second condition: If word already exists for a pattern and vice versa.
# Time complexity: O(m*(m+n)), Space complexity O(m+n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        m, n = len(pattern), len(s_split)
        if m != n: return False

        seen_pattern, seen_s = dict(), dict()
        for i, p in enumerate(pattern):
            if p not in seen_pattern and s_split[i] not in seen_s:
                seen_pattern[p] = s_split[i]
                seen_s[s_split[i]] = p
            elif p not in seen_pattern or s_split[i] not in seen_s \
                    or seen_pattern[p] != s_split[i] or seen_s[s_split[i]] != p:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))  # True
    print(sol.wordPattern(pattern="abba", s="dog dog dog dog"))  # False
    print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))  # False
    print(sol.wordPattern(pattern="aba", s="dog cat cat"))  # False
