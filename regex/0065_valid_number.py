# https://leetcode.com/problems/valid-number/
# tags: #string, #linkedin, #microsoft, #simulation
#
# Solution 1: DFA (Deterministic Finite Automaton)
# https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
# Time Complexity: O(n), Space complexity: O(1)
#
# Solution 2: Regex (For reference purpose)
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        states = [{},
                  {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                  {'digit': 3, '.': 4},
                  {'digit': 3, '.': 5, 'e': 6, 'E': 6, 'blank': 9},
                  {'digit': 5},
                  {'digit': 5, 'e': 6, 'E': 6, 'blank': 9},
                  {'sign': 7, 'digit': 8},
                  {'digit': 8},
                  {'digit': 8, 'blank': 9},
                  {'blank': 9}]
        state = 1
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            if c not in states[state]:
                return False
            state = states[state][c]
        if state not in [3, 5, 8, 9]:
            return False
        return True

    def isNumber_regex(self, s: str) -> bool:
        pattern = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
        return pattern.match(s.strip(" ")) is not None


if __name__ == "__main__":
    sol = Solution()
    valid_numbers = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
                     "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    invalid_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "+++"]

    for num in valid_numbers:
        print(num, sol.isNumber_regex(num))

    for num in invalid_numbers:
        print(num, sol.isNumber_regex(num))
