# https://leetcode.com/problems/strobogrammatic-number-ii/
# tags: #google
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)
# For example, the numbers "69", "88", and "818" are all strobogrammatic
#
# There are 2 constraints we need to be aware about: No 6/9 in the middle and no 0 at the extremes
# The solution can be solved through backtracking constructing the number from the extremes to the middle
# starting at (0, n-1) and go inward iterating all the keys in the strobogrammatic dictionary
# Time complexity: O(5^(n/2)), Space complexity: O(5^(n/2)) due to recursive stack trace
from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobogrammatic_dict = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        result = []

        def backtracking(start, end, weave) -> None:
            if start > end:
                result.append("".join(weave))
                return

            for num_key in strobogrammatic_dict.keys():
                if (start != end and num_key == "0" and start == 0) or (start == end and num_key in ("6", "9")):
                    continue

                weave[start], weave[end] = num_key, strobogrammatic_dict[num_key]
                backtracking(start + 1, end - 1, weave)

        backtracking(0, n - 1, [None] * n)
        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.findStrobogrammatic(n=1))  # ["0","1","8"]
    print(sol.findStrobogrammatic(n=2))  # ["11","69","88","96"]
    print(sol.findStrobogrammatic(n=3))
