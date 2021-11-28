# https://leetcode.com/problems/all-paths-from-source-to-target/
# tags: #backtracking, #bfs, #dfs, #graph
#
# Solution 1: DFS + Backtracking
# Classical backtracking problem used to traverse the graph to find all possible paths
# Time complexity: O(n*2^n), Space complexity O(n) required by max recursive stack depth and for storing path
#
# Solution 2: BFS
# We can start from the starting node 0 and traverse every possible next node from the current node.
# Whenever we reach the last node n-1, we will add the path till now into the final answer.
# Time complexity: O(n*2^n), Space complexity O(n*2^n)
from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtracking(u: int, weave: List[int]) -> None:
            if u == n - 1:
                paths.append(weave)
                return None

            for v in graph[u]:
                backtracking(v, weave + [v])

        paths = []
        n = len(graph)
        backtracking(0, [0])
        return paths

    def allPathsSourceTarget_bfs(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        queue = deque([[0]])
        n = len(graph)

        while queue:
            path = queue.popleft()
            if path[-1] == n - 1: paths.append(path)
            else: queue.extend(path + [neighbor] for neighbor in graph[path[-1]])

        return paths


if __name__ == "__main__":
    sol = Solution()
    print(sol.allPathsSourceTarget_bfs(graph=[[1, 2], [3], [3], []]))  # [[0,1,3],[0,2,3]]

    print(sol.allPathsSourceTarget_bfs(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
    # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
