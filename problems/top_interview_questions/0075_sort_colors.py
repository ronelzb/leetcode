# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    # Solution: Dutch partitioning problem (https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
    # Leetcode solution:
    # https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1


if __name__ == "__main__":
    sol = Solution()

    colors = [2, 0, 2, 1, 1, 0]
    sol.sortColors(colors)
    print(colors)  # [0,0,1,1,2,2]
