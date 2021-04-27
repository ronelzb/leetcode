# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_last_index = dict()
        max_length = start_index = 0

        for i, c in enumerate(s):
            if c in char_last_index:
                start_index = max(start_index, char_last_index[c] + 1)

            max_length = max(max_length, i + 1 - start_index)
            char_last_index[c] = i

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert sol.lengthOfLongestSubstring(s="bbbbb") == 1
    assert sol.lengthOfLongestSubstring(s="abba") == 2
    assert sol.lengthOfLongestSubstring(s="") == 0
