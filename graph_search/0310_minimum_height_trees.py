# https://leetcode.com/problems/minimum-height-trees/
# tags: #bfs, #dfs, #topological_sort
#
# Solution: BFS + Topological sort
# Begin with external nodes: nodes only connected to one element.
# Find the next external nodes and replace current external nodes with current,
# repeat until next external nodes are empty, using a modified topological sort algorithm for undirected graphs.
# Basically, the idea is to eat up all the leaves at the same time, until one/two leaves are left.
# Time complexity: O(n), Space complexity: O(n)
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        q = deque()
        for node, edges in graph.items():
            if len(edges) == 1:
                q.append(node)

        while n > 2:
            n -= len(q)  # remove leaves
            next_leaves = deque()

            # process current layer leaves to find next leaves
            while q:
                leave = q.popleft()
                for node in graph[leave]:
                    graph[node].remove(leave)

                    if len(graph[node]) == 1:
                        next_leaves.append(node)

            q = next_leaves

        return list(q)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))  # [1]
