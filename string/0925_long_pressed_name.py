# https://leetcode.com/problems/long-pressed-name/
# tags: #google, #string, #two_pointers
class Solution:
    # Classical two pointers problem where an interesting idea is to loop through
    # typed comparing each value to name[i], eventually we should've reached the end of name
    # Time complexity: O(m) m=typed, Space complexity: O(1)
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = len(name), len(typed)
        if m < n:
            return False

        i = 0
        for j in range(m):
            if i < n and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False

        return i == n


if __name__ == "__main__":
    sol = Solution()

    print(sol.isLongPressedName(name="alex", typed="aaleex"))  # True
    print(sol.isLongPressedName(name="saeed", typed="ssaaedd"))  # False
