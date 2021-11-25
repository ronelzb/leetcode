# https://leetcode.com/problems/verifying-an-alien-dictionary/
# tags: #array, #hash_table, #string
#
# Solution: Check adjacent words
# Create a dictionary, key is each word in new order, value is its index, which means its new position in the new order.
# Transform the list of words into its index in new order.
# When comparing each char for each adjacent word we have 3 options:
# * If previous > current it means current word is lexicographically less than previous thus return False
# * If previous < current it means current word is lexicographically greater than previous thus break this comparison
# * If they are equal go to the next set of letters
# If we reach the end of any of the compared words we need to check if previous word is greater than current
# Time complexity: O(w*n) n=max(w[i], w[i-1]) at each i, Space complexity O(c), c=26 => O(1)
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {c: i for i, c in enumerate(order)}
        for w in range(1, len(words)):
            i, j, m, n = 0, 0, len(words[w - 1]), len(words[w])

            while i < m and j < n:
                first_word_idx = char_order[words[w - 1][i]]
                second_word_idx = char_order[words[w][j]]

                if first_word_idx > second_word_idx:
                    return False
                elif first_word_idx < second_word_idx:
                    break

                i += 1
                j += 1

            if i < m and j == n:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))  # True
