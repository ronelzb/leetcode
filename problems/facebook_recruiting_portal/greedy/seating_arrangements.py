# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2444722699191194&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n*log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def minOverallAwkwardness(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, n):
            diff = max(diff, arr[i] - arr[i - 2])
        # for i in range(3, n):
        #     diff = max(diff, arr[i] - arr[i - 2])

        return max(diff, arr[n - 1] - arr[n - 2])


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOverallAwkwardness(arr=[5, 10, 6, 8]))  # 4
    print(sol.minOverallAwkwardness(arr=[2, 4, 6, 20, 40]))  # 34
    print(sol.minOverallAwkwardness(arr=[1, 3, 5, 7, 9, 10, 8, 6, 4, 2]))  # 2
