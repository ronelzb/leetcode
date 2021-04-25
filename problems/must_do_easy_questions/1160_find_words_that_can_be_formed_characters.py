from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_words = 0
        c = Counter(chars)

        for word in words:
            current_count = 0

            for key, value in Counter(word).items():
                if c.get(key, 0) - value < 0:
                    current_count = 0
                    break
                current_count += value

            count_words += current_count

        return count_words


if __name__ == "__main__":
    sol = Solution()
    assert sol.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
    assert sol.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10
