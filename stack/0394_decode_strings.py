# https://leetcode.com/problems/decode-string/
# tags: #google, #stack, #queue, #sliding_window
from collections import deque


class Solution:

    # There is 2 approaches to solve this problem: brackets stack or sliding window
    # I took the sliding window approach to be more efficient space complexity wise
    # Also, there is a couple of edge cases we need to be aware of:
    # 1. Substring Multiplier can be over 1 digit (e.g: 10, 100).
    # 2. Nested substrings can be found one after the other
    # Sliding window is doing the enqueue finding the parent substring and then doing the recursion
    # When it finishes building the substring we need to multiply it k times
    # Time complexity: O(n * k_max), Space complexity: O(k_max) k_max times doing the recursion
    def decodeString(self, s: str) -> str:
        def decode_substring(mult, start, end) -> str:
            substring = ""

            while start < end:
                if s[start].isnumeric():
                    sub_start = start
                    while s[start].isnumeric():
                        start += 1

                    sub_multiplier = int(s[sub_start:start])
                    start += 1
                    sub_start = start
                    opening_brackets = 1

                    while opening_brackets > 0:
                        if s[start] == "[":
                            opening_brackets += 1
                        elif s[start] == "]":
                            opening_brackets -= 1
                        start += 1 if opening_brackets > 0 else 0
                    substring += decode_substring(sub_multiplier, sub_start, start)
                else:
                    substring += s[start]
                start += 1

            substring *= mult
            return substring

        return decode_substring(1, 0, len(s))

    def decodeStringStack(self, s: str) -> str:
        stack = deque()
        multiplier, current_decoded = 0, ""

        for c in s:
            if c == "[":
                stack.append((multiplier, current_decoded))
                current_decoded = ""
                multiplier = 0
            elif c == "]":
                num, prev_decoded = stack.pop()
                current_decoded = prev_decoded + num * current_decoded
            elif c.isdigit():
                multiplier = multiplier * 10 + int(c)
            else:
                current_decoded += c

        return current_decoded

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeStringStack(s="3[a]2[bc]"))  # "aaabcbc"
    print(sol.decodeStringStack(s="3[a2[c]]"))  # "accaccacc"
    print(sol.decodeStringStack(s="2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(sol.decodeStringStack(s="100[leetcode]"))  # 100 * "leetcode"
