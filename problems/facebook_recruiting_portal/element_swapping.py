# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=838749853303393&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n^2), Space complexity: O(1)
from typing import List


class Solution:
    def findMinArray(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return arr
        i, n = 0, len(arr)
        while k > 0 and i < n:
            sub_len = min(k, n - i - 1)
            min_num, min_idx = arr[i], i

            for j in range(i + 1, sub_len + i + 1):
                if arr[j] < min_num:
                    min_num, min_idx = arr[j], j

            for x in range(min_idx, i, -1):
                arr[x], arr[x - 1] = arr[x - 1], arr[x]

            k -= min_idx - i
            i += 1

        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArray(arr=[5, 3, 1], k=2))  # [1, 5, 3]
    print(sol.findMinArray(arr=[8, 9, 11, 2, 1], k=3))  # [2, 8, 9, 11, 1]
    print(sol.findMinArray(arr=[1, 1, 8, 1, 11, 2, 1], k=7))  # [1, 1, 1, 1, 2, 8, 11]
    print(sol.findMinArray(arr=[5, 2, 3, 6, 3, 1], k=3))  # [2, 3, 5, 3, 6, 1]
