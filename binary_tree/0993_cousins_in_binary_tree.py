# https://leetcode.com/problems/cousins-in-binary-tree/
# tags: #bfs, #binary_tree, #dfs
#
# Solution 1: DFS
# Traverse the binary tree finding x and y attributes individually
# The statement dfs(left) or dfs(right) only passes the one that is not None.
# So, from each call of the root you only find one of the variables.
# Then you compare their level and parents to say if they are cousins or not.
# Time Complexity: O(n), Space complexity: O(n)
#
# Solution 2 : BFS
# Store the parent and level information here while performing BFS and break early once you have both x and y attributes
# Time Complexity: O(n), Space complexity: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode], level: int, lookup: int) -> tuple:
            if node:
                if node.val == lookup:
                    return parent, level

                return dfs(node.left, node, level + 1, lookup) or dfs(node.right, node, level + 1, lookup)

        x_parent, x_level, y_parent, y_level = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return x_level == y_level and x_parent != y_parent

    def isCousins_bfs(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_parent, x_level, y_parent, y_level = None, 0, None, 0
        queue = deque([(root, 0, None)])

        while queue:
            node, level, parent = queue.popleft()
            if node.val == x: x_parent, x_level = parent, level
            if node.val == y: y_parent, y_level = parent, level

            if x_parent and y_parent: break
            if node.left: queue.append((node.left, level + 1, node))
            if node.right: queue.append((node.right, level + 1, node))

        return x_level == y_level and x_parent != y_parent


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.right = TreeNode(4)
    r.right = TreeNode(3)
    r.right.right = TreeNode(5)
    print(sol.isCousins_bfs(root=r, x=5, y=4))  # True
