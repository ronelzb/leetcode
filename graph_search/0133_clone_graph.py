# https://leetcode.com/problems/clone-graph/
# tags: #bfs, #blind_75_must_do, #dfs, #graph, #hash_table
#
# Solution 1: BFS
# Overall approach is graph traversal. The trick is in cloning.
# 1. Use a dictionary with node as key and the clone as value
# 2. When visiting the neighbors, create a key-value pair for each child node.
# 3. Add that key value pair to the neighbor for the parent node if that neighboring node has not been visited.
# Ensuring that the neighboring node is not visited as we are dealing with an undirected graph
# 4. Return the value of the node being passed in
# Time complexity: O(V*E), Space complexity O(V)
#
# Solution 2: DFS recursive
# Time complexity: O(V*E), Space complexity O(V)
#
# # Solution 3: DFS iterative
# # Time complexity: O(V*E), Space complexity O(V)
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"{self.val} -> [{', '.join([str(n.val) for n in self.neighbors])}]"


class Solution:
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        if not node: return node
        graph = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in graph:
                    queue.append(neighbor)
                    graph[neighbor] = Node(neighbor.val)
                graph[current].neighbors.append(graph[neighbor])

        return graph[node]

    def cloneGraph_dfs_recur(self, node: 'Node') -> 'Node':
        if not node: return node
        graph = {node: Node(node.val)}

        def dfs(current: 'Node') -> None:
            for neighbor in current.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                    dfs(neighbor)
                graph[current].neighbors.append(graph[neighbor])

        dfs(node)
        return graph[node]

    def cloneGraph_dfs_iter(self, node: 'Node') -> 'Node':
        if not node: return node
        graph = {node: Node(node.val)}
        stack = deque([node])

        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in graph:
                    stack.append(neighbor)
                    graph[neighbor] = Node(neighbor.val)
                graph[current].neighbors.append(graph[neighbor])

        return graph[node]


if __name__ == "__main__":
    sol = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print(sol.cloneGraph_dfs_recur(node1))
