# https://leetcode.com/problems/3sum-with-multiplicity/
# tags: #array, #counting, #hash_table, #sorting, #two_pointers
#
# Solution: Sorting + Two pointers
# Time complexity: O(n^2), Space complexity O(1)
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        res, n = 0, len(arr)

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                if arr[i] + arr[j] + arr[k] > target:
                    k -= 1
                elif arr[i] + arr[j] + arr[k] < target:
                    j += 1
                else:
                    left = right = 1
                    while j + left < k and arr[j] == arr[j + left]:
                        left += 1
                    while j + left <= k - right and arr[k] == arr[k - right]:
                        right += 1

                    mult = (left + right) * (left + right - 1) // 2 if arr[j] == arr[k] else left * right
                    res += mult
                    j += left
                    k -= right

        return res % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))  # 20
