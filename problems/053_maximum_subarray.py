from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, new_max = 0, 0

        for i in range(len(nums)):
            new_max += nums[i]

            if new_max < 0:
                new_max = 0
            elif new_max > current_max:
                current_max = new_max

        return current_max

    def max_sub_array_dp(self, nums: List[int]) -> int:
        current_max, new_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], new_max + nums[i])
            current_max = max(current_max, new_max)

        return current_max

    def max_sub_array_divide_and_conquer(self, nums: List[int], left=0, right=None) -> int:
        if right is None:
            right = len(nums) - 1

        if left == right:
            return nums[left]

        middle = (left + right) // 2

        def _max_crossing_sum(nums, left, middle, right):
            current = 0
            max_left = float("-inf")

            for i in range(middle, left - 1, -1):
                current += nums[i]
                if current > max_left:
                    max_left = current

            current = 0
            max_right = float("-inf")
            for i in range(middle + 1, right + 1):
                current += nums[i]
                if current > max_right:
                    max_right = current

            return max(max_left, max_right, max_left + max_right)

        return max(self.max_sub_array_divide_and_conquer(nums, left, middle),
                   self.max_sub_array_divide_and_conquer(nums, middle + 1, right),
                   _max_crossing_sum(nums, left, middle, right))


if __name__ == "__main__":
    sol = Solution()

    print(sol.max_sub_array_divide_and_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # [4,-1,2,1] = 6
    print(sol.max_sub_array_divide_and_conquer([5, 4, -1, 7, 8]))  # [5,4,-1,7,8] = 23
