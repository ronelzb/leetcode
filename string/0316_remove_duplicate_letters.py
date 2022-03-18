# https://leetcode.com/problems/remove-duplicate-letters/
# tags: #greedy, #monotonic_stack, #stack, #string
#
# Solution: Monotonic Stack + Greedy
# Find each letter last occurrence in the input string
# Iterate over the string and if a letter is already seen continue to the next letter
# Then, we apply the conditions for a monotonic stack:
# * If the evaluated letter is less than previous (top of the stack) and also if the last occurrence of that
# previous symbol is greater than current i
# * Then, remove the previous letter from both the stack and seen
# Later, append the new letter to our stack and mark it as seen.
# Eventually, return the result stack.
# Time complexity: O(n), Space complexity: O(26) => O(1)
from collections import deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrences = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = deque()

        for i, c in enumerate(s):
            if c in seen: continue

            while stack and c < stack[-1] and last_occurrences[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicateLetters(s="bcabca"))  # "abc"
    print(sol.removeDuplicateLetters(s="bcdbc"))  # "bcd"
