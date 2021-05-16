# https://leetcode.com/problems/clone-graph/
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"{self.val} -> [{', '.join([str(n.val) for n in self.neighbors])}]"


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        visited = dict()
        cloned_node = Node(node.val)
        q = deque([node])
        visited[node.val] = cloned_node

        while q:
            current = q.popleft()

            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    neighbor_cloned = Node(neighbor.val)
                    q.append(neighbor)
                    visited[neighbor.val] = neighbor_cloned

                visited[current.val].neighbors.append(visited[neighbor.val])

        return cloned_node


if __name__ == "__main__":
    sol = Solution()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    new1 = sol.cloneGraph(n1)
