# https://leetcode.com/problems/critical-connections-in-a-network/
# tags: #dfs
#
# Solution: Tarjan's strongly connected components (DFS)
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# In Tarjan's algorithm we do a recursive DFS on our graph and for each node, we keep track of the earliest node that
# we can circle back around to reach. By doing this, we can identify whether a given edge is a bridge because the far
# node doesn't lead back to any other earlier node.
# For our recursive dfs method, each newly-visited node should set its initial value for both disc and low to
# the current value of time before time is incremented.
# Then we recursively call dfs on each of the unvisited adjacent nodes of the current node . If one of the possible
# next nodes is an earlier node (disc[next] < curr[low]), then we've found a loop and we should update the low value
# for the current node. As each layer of the recursive function backtracks, it will propagate this value of low back
# down the chain.
# Time complexity: O(V+E), Space complexity: O(V+E)
from collections import defaultdict
from typing import List


class Solution:
    iterations = 0

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, parent: int) -> None:
            if disc[node] > 0: return

            disc[node] = low[node] = self.iterations
            self.iterations += 1
            for neighbor in graph[node]:
                if disc[neighbor] == 0: dfs(neighbor, node)

            # minimal num in the neighbors, exclude the parent
            low[node] = min([low[neighbor] for neighbor in graph[node] if neighbor != parent] + [disc[node]])

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [0] * n
        low = [0] * n
        self.iterations = 1
        dfs(0, -1)

        res = []
        for u, v in connections:
            if low[u] > disc[v] or low[v] > disc[u]:
                res.append([u, v])

        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))  # [[1,3]]
    print(s.criticalConnections(n=2, connections=[[0, 1]]))  # [[0,1]]
