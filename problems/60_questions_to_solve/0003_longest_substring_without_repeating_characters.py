# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:

    # Use sliding window technique to solve this problem
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

    # Optimal variant: Instead of counting each chars we will store where each char was last seen
    # Sliding window will be moving by where each last seen char thus O(1) pass
    # Be careful when getting start from max(start, char_last_seen), e.g: abba
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
