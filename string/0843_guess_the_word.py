# https://leetcode.com/problems/maximum-number-of-visible-points/
# tags: #game_theory, #google, #interactive, #math, #string
#
# Solution: Game Theory
# https://leetcode.com/problems/guess-the-word/discuss/556075/How-to-explain-to-interviewer-843.-Guess-the-Word
# Time complexity: O(n), Space complexity O(n)
import random
from typing import List


class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def get_match(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    count += 1
            return count

        i, matches = 0, 0
        word = None
        while i < 10 and matches != 6:
            random_index = random.randint(0, len(wordlist) - 1)
            word = wordlist[random_index]
            matches = master.guess(word)
            candidates = []

            for w in wordlist:
                if matches == get_match(word, w):
                    candidates.append(w)
            wordlist = candidates
        return word
