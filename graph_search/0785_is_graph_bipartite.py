# https://leetcode.com/problems/is-graph-bipartite/
# tags: #bfs, #dfs, #graph, #union_find
#
# Solution: DFS + nodes coloring
# Constraint: A graph is bipartite if each edges connects only a pair of nodes
# We can solve this problem using nodes coloring solution where we color each edge as
# [v,u] = 1 - [u,v] (Color it with the color opposite to color[u])
# Time complexity: O(V + E), Space complexity O(V + E)
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(u: int) -> bool:
            for v in graph[u]:
                if v in color:
                    if color[v] == color[u]: return False
                else:
                    color[v] = 1 - color[u]
                    if not dfs(v): return False
            return True

        color = dict()
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i): return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
    print(sol.isBipartite())
