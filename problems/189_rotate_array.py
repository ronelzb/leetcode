from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        if k == 0:
            return

        i, count = 0, 0
        while count < n:
            new_position = (i + k) % n
            temp = nums[new_position]
            nums[new_position] = nums[i]
            count += 1
            j = new_position

            while j != i and count < n:
                new_position = (j + k) % n
                nums[new_position], temp = temp, nums[new_position]
                j = new_position
                count += 1

            i += 1


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(array, k=3)
    assert array == [5, 6, 7, 1, 2, 3, 4]
