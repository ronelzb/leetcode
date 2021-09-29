# https://leetcode.com/problems/sort-array-by-parity-ii/
# tags: #array, #sorting, #two_pointers
#
# Solution 1: Sort array by parity
# Make a new array of the same length as nums, traverse nums storing even/odds in the corresponding index
# Time complexity: O(n*log(n)), Space complexity: O(n)
#
# Solution 2: Two pointers
# Create two pointers: One for evens and one for odds, at each point of the iteration check if both numbers
# under the pointers are misplaced and swap them, if one them is misplaced move the other pointer
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def sortArrayByParityII_sorting(self, nums: List[int]) -> List[int]:
        even, odd, n = 0, 1, len(nums)
        res = [0] * n

        for num in nums:
            if num % 2 == 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2

        return res

    def sortArrayByParityII_twoPointer(self, nums: List[int]) -> List[int]:
        even, odd, n = 0, 1, len(nums)

        while odd < n and even < n:
            if nums[even] % 2 != 0 and nums[odd] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
            elif nums[even] % 2 != 0:
                odd += 2
            elif nums[odd] % 2 == 0:
                even += 2
            else:
                even += 2
                odd += 2

        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArrayByParityII_sorting(nums=[4, 2, 5, 7]))  # [4,5,2,7] || [4,7,2,5] || [2,5,4,7] || [2,7,4,5]
    print(sol.sortArrayByParityII_sorting(nums=[2, 3]))  # [2,3]
    print(sol.sortArrayByParityII_sorting(nums=[648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))  # [648,831,560,997,192,
    # 897,986,829,424,843]
