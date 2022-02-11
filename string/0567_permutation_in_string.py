# https://leetcode.com/problems/permutation-in-string/
# tags: #hash_table, #sliding_window, #string, two_pointers
#
# Solution: Counter + Sliding Window
# Count the elements on s1 and the first len(s1) elements on s2
# Iterate from len(s1) to len(s2) checking if the counters are equals
# If not, add the current element and subtract the "tail" element from s2 counter
# The tail element would be i - len(s1)
# If a letter in the s2 counter reaches zero remove the letter to keep consistency
# Time complexity: O(m+n), Space complexity O(n)
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:m])

        for i in range(m, n):
            if s1_counter == s2_counter: return True

            s2_counter[s2[i]] += 1
            s2_counter[s2[i - m]] -= 1
            if s2_counter[s2[i - m]] == 0: del s2_counter[s2[i - m]]

        if s1_counter == s2_counter: return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion(s1="ab", s2="eidbaooo"))  # True
