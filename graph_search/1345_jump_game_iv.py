# https://leetcode.com/problems/jump-game-iv/
# tags: #bfs, #hash_table
#
# Solution: Breadth-first search
# Create a graph pointing each number to the list of indexes in the array they are located.
# We traverse the graph using a classical bfs making 3 moves:
# * i - 1, i + 1 based on the current position.
# * Find and enqueue all the other indexes the current number is located
# (we appended the list of indexes at the graph init). Empty the list, so we don't traverse them twice
# Time complexity: O(n), Space complexity O(n)
from collections import defaultdict, deque

from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = defaultdict(list)
        queue = deque([(0, 0)])
        seen = set()

        for i, num in enumerate(arr):
            graph[num].append(i)

        while queue:
            step, k = queue.popleft()
            if k == n - 1:
                return step

            for i in range(k - 1, k + 2):
                if n > i >= 0 and i not in seen:
                    seen.add(i)
                    queue.append((step + 1, i))

            if graph[arr[k]]:
                for num_index in graph[arr[k]]:
                    if num_index not in seen:
                        seen.add(num_index)
                        queue.append((step + 1, num_index))
                graph[arr[k]] = []

        return n - 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))  # 3
    print(sol.minJumps(arr=[6, 1, 9]))  # 2
    print(sol.minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))  # 3
