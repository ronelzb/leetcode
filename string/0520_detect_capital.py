# https://leetcode.com/problems/detect-capital/
# tags: #string
#
# Solution 1: One pass
# At the beginning check if the first letter is capital, then check the second letter
# For each subsequent letter follow the rules
# 1. Everything can be upper-case "LEETCODE"
# 2. 1st character is capital then everything is lowercase "Leetcode"
# 3. Everything is lowercase "leetcode"
# Time complexity: O(n), Space complexity O(1)
#
# Solution 2: Python built-in methods
# Time complexity: O(n), Space complexity O(1)
#
# Solution 3: Count capitals
# Using the rules we can infer 3 conditions to be True:
# 1. No capital letters found
# 2. All capital letters
# 3. Only 1 capital letter being the first char
# Time complexity: O(n), Space complexity O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def is_capital(c: str) -> bool: return 65 <= ord(c) <= 90

        n = len(word)
        first_capital = is_capital(word[0])
        second_capital = False

        for i in range(1, n):
            is_current_capital = is_capital(word[i])

            if not first_capital and is_current_capital: return False
            if i == 1: second_capital = is_current_capital
            if (first_capital and second_capital and not is_current_capital) \
                or (first_capital and not second_capital and is_current_capital): return False

        return True

    def detectCapitalUse_builtin(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()

    def detectCapitalUse_countCapitals(self, word: str) -> bool:
        capitals = sum(c.isupper() for c in word)
        return capitals == 0 or capitals == len(word) or (capitals == 1 and word[0].isupper())


if __name__ == "__main__":
    sol = Solution()
    print(sol.detectCapitalUse_countCapitals(word="USA"))  # True
    print(sol.detectCapitalUse_countCapitals(word="leetcode"))  # True
    print(sol.detectCapitalUse_countCapitals(word="Google"))  # True
    print(sol.detectCapitalUse_countCapitals(word="FlaG"))  # False
    print(sol.detectCapitalUse_countCapitals(word="mL"))  # False
