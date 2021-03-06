# https://leetcode.com/problems/container-with-most-water/
# #array, #greedy, #two_pointers
#
# Start by initializing two pointers at both ends of the array.
# Every time move the smaller value pointer to inner array.
#
# "By moving shorter end pointer further doesn't eliminate the final answer (with two ends at maxi, maxj respectively)
# in our process"
# We know as we move any pointer further, the length of the next rectangle decreases,
# so the height needs to increase as to result in a larger area
# min(height[maxi], height[maxj]) > min(height[i], height[j])
#
# So the smaller one in height[i], height[j] won't become any end in the maximum rectangle,
# so it's safe to move forward without it
#
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = max_area = 0
        end = len(height) - 1

        while start < end:
            max_area = max((end - start) * min(height[start], height[end]), max_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea(height=[4, 3, 2, 1, 4]) == 16
    assert sol.maxArea(height=[1, 2, 4, 3]) == 4
    assert sol.maxArea(height=[2, 3, 10, 5, 7, 8, 9]) == 36
