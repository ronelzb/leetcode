# https://leetcode.com/problems/guess-number-higher-or-lower/
# tags: #binary_search
#
# Solution: Binary Search
# Time Complexity: O(log(n)), Space complexity: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(num: int) -> int:
            pick = 6  # example
            if pick < num:
                return -1
            elif pick > num:
                return 1
            else:
                return 0

        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            current_guess = guess(middle)

            if current_guess == 0:
                return middle
            elif current_guess > 0:
                left = middle + 1
            else:
                right = middle - 1

        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.guessNumber(n=10))  # Solution
