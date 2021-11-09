# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=229890198389794&c=896138004629128&ppid=454615229006519&practice_plan=0
# Create an queue where you save each element's index along with its value.
# Step 2: Iterate through the given queue x times.
# Store x elements into a temp list.
# Check the maximum element when iterating.
# Save the index of the maximum element in result list.
# Remove the maximum element from the temp list.
# Add the remaining elements previously saved in the popped list back to the queue.
# Repeat Step 2 until x becomes 0.
# Time complexity: O(x^2), Space complexity O(n)
import sys
from collections import deque
from typing import List


class Solution:
    def findPositions(self, arr: List[int], x: int) -> List[int]:
        queue = deque([(i + 1, num) for i, num in enumerate(arr)])
        res = []

        for _ in range(x):
            max_num = -(sys.maxsize - 1)
            popped = []

            j, maxj, max_idx = 0, 0, -1
            while queue and j < x:
                idx, num = queue.popleft()
                if num > max_num:
                    max_num = num
                    max_idx = idx
                    maxj = j

                popped.append((idx, max(0, num - 1)))
                j += 1

            if popped:
                popped.pop(maxj)

            queue.extend(popped)
            res.append(max_idx)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPositions(arr=[1, 2, 2, 3, 4, 5], x=5))  # [5, 6, 4, 1, 2]
