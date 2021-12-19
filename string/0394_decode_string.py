# https://leetcode.com/problems/decode-string/
# tags: #dfs, #stack, #string
#
# Solution 1: Recursion
# Traverse the string appending each non-digit char found until you find a digit and do the following:
# * Find the total length of the int in the substring and parse it (we'll need to use it later)
# * Start traversing the substring after the first opening bracket, count the opening and closing brackets
# * When count reaches zero then it's time to recurse from the first opening bracket to the current index
# * Eventually, when the recursion finishes multiply the result encoded string with the last digit found
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: Stack
# When we hit an open bracket, we know we have parsed k for the contents of the bracket, so
# push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
# the enclosed string k times.
# Time complexity: O(n), Space complexity O(n)
from collections import deque


class Solution:
    def decodeString_recursion(self, s: str, start: int = 0, end: int = None) -> str:
        if end is None:
            end = len(s)

        res = []
        while start < end:
            if s[start].isdigit():
                digit_start = start
                while s[start].isdigit(): start += 1
                mult = int(s[digit_start: start])
                encoded_start = start = start + 1

                count_brackets = 1
                while count_brackets:
                    if s[start] == "[": count_brackets += 1
                    if s[start] == "]": count_brackets -= 1
                    if count_brackets: start += 1
                encoded_str = self.decodeString_recursion(s, encoded_start, start)

                res.append(encoded_str * mult)
            else:
                res.append(s[start])

            start += 1

        return "".join(res)

    def decodeString_stack(self, s: str) -> str:
        current_str = ""
        stack = deque()
        k = 0

        for c in s:
            if c == "[":
                stack.append((current_str, k))
                current_str = ""
                k = 0
            elif c == "]":
                last_str, last_k = stack.pop()
                current_str = last_str + last_k * current_str
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                current_str += c

        return current_str


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString_stack(s="3[a]2[bc]"))  # "aaabcbc"
    print(sol.decodeString_stack(s="3[a2[c]]"))  # "accaccacc"
    print(sol.decodeString_stack(s="2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(sol.decodeString_stack(s="abc3[cd]xyz"))  # "abccdcdcdxyz"
    print(sol.decodeString_stack(s="100[leetcode]"))  #
