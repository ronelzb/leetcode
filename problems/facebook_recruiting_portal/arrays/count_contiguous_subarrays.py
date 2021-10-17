# Time Complexity: O(n), Space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def count_subarrays(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        stack = deque()

        for i, num in enumerate(arr):
            while stack and num > arr[stack[-1]]:
                result[i] += result[stack.pop()]
            stack.append(i)
            result[i] += 1

        stack.clear()
        temp = [0] * n
        for i, num in reversed(list(enumerate(arr))):
            while stack and num > arr[stack[-1]]:
                idx = stack.pop()
                result[i] += temp[idx]
                temp[i] += temp[idx]
            stack.append(i)
            temp[i] += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.count_subarrays([3, 4, 1, 6, 2]) == [1, 3, 1, 5, 1]
    # assert sol.rotationalCipher("abcdZXYzxy-999.@", 200) == "stuvRPQrpq-999.@"
