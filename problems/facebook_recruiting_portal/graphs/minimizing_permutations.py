# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=292715105029046&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time complexity: O(n*log(n) + n!) => O(n!), Space complexity O(n)
from collections import deque
from typing import List


class Solution:
    def minOperations(self, arr: List[int]) -> int:
        target = "".join([str(num) for num in sorted(arr)])
        curr = "".join([str(num) for num in arr])
        queue = deque([(0, curr)])
        visited = {curr}

        while queue:
            level, curr = queue.popleft()

            if curr == target:
                return level

            for i in range(len(curr)):
                for j in range(i, len(curr)):
                    permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]

                    if permutation not in visited:
                        visited.add(permutation)
                        queue.append((level + 1, permutation))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([1, 2, 5, 4, 3]))  # 1
    print(sol.minOperations([3, 1, 2]))  # 2
