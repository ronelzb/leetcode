# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# tags: #hash_table, #linked_list, #sliding_window, #string
#
# Use sliding window technique to solve this problem, using a dictionary which stores the characters in string
# as keys and their positions as values, and keep two pointers which define the max substring.
# Move the right pointer to scan through the string
#
# Optimal variant: Instead of counting each chars we will store where each char was last seen
# Sliding window will be moving by where each last seen char thus O(1) pass
# Be careful when getting start from max(start, char_last_seen), e.g: abba
#
# Optimal Time complexity: O(n), Space complexity: O(1) distinct chars seen in word
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length = 0, 0
        counter_chars = {}

        for i, c in enumerate(s):
            counter_chars.setdefault(c, 0)
            counter_chars[c] += 1

            while counter_chars[c] > 1:
                counter_chars[s[start]] -= 1
                start += 1

            max_length = max(max_length, i - start + 1)

        return max_length

    def lengthOfLongestSubstring_optimal(self, s: str) -> int:
        start, max_length = 0, 0
        char_last_seen = {}

        for i, c in enumerate(s):
            if c in char_last_seen:
                start = max(start, char_last_seen[c] + 1)

            char_last_seen[c] = i
            max_length = max(max_length, i - start + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring_optimal(s="abcabcbb") == 3
    assert sol.lengthOfLongestSubstring_optimal(s="bbbbb") == 1
    assert sol.lengthOfLongestSubstring_optimal(s="") == 0
    assert sol.lengthOfLongestSubstring_optimal(s="pwwkew") == 3
    assert sol.lengthOfLongestSubstring_optimal(s="abba") == 2
