# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=226994905008716&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n*log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def balancedSplitExists(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 1: return False

        arr.sort()
        left_sum, right_sum = sum(arr), 0

        for i in range(n - 1, 0, -1):
            left_sum -= arr[i]
            right_sum += arr[i]
            if left_sum == right_sum and arr[i - 1] < arr[i]:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.balancedSplitExists(arr=[1, 5, 7, 1]))  # True
    print(sol.balancedSplitExists(arr=[12, 7, 6, 7, 6]))  # False
