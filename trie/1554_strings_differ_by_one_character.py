# https://leetcode.com/problems/strings-differ-by-one-character/
# tags: #google, #hash_table, #rolling_hash
#
# Solution: Trie
# Implement a trie data structure
# For each word, traverse the trie trying to find a leave node in which the mismatch count == 1
# Time complexity: O(n*m), Space complexity O(sum(n))
from typing import List


class Solution:
    def differByOne(self, d: List[str]) -> bool:
        def search_word(w: str, current: dict, idx: int, mismatch_count: int) -> bool:
            if "#" in current:
                return mismatch_count == 1

            for child, child_nodes in current.items():
                is_diff = child != w[idx]
                if mismatch_count + is_diff <= 1 and search_word(w, child_nodes, idx + 1, mismatch_count + is_diff):
                    return True

            return False

        trie = dict()

        for word in d:
            current = trie
            for c in word:
                current.setdefault(c, dict())
                current = current[c]
            current["#"] = True

        for word in d:
            if search_word(word, trie, 0, 0):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.differByOne(d=["abcd", "acbd", "aacd"]))  # True
    print(sol.differByOne(d=["ab", "cd", "yz"]))  # False
    print(sol.differByOne(d=["abcd", "cccc", "abyd", "abab"]))  # True
    print(sol.differByOne(d=["aaaddb", "aaaacd", "aaacda", "aaaaba", "aaaccd"]))  # True
