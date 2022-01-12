# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# tags: #dfs
#
# Solution 1: Iterative
# Traverse the tree using the main property of the Binary Search Tree: smaller values go to the left,
# greater values go to the right, until we reach a leaf node.
# Time complexity: O(log(n)), Space complexity O(1)
#
# Solution 2: Recursion
# Traverse the tree using DFS following Binary Search Tree property.
# Time complexity: O(log(n), Space complexity O(h)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            return new_node

        current = root
        while current:
            if current.val > val:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            elif current.val < val:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right

        return root

    def insertIntoBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST_recursive(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST_recursive(root.right, val)
        return root


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(4)
    t.left = TreeNode(2)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right = TreeNode(7)
    sol.insertIntoBST_recursive(root=t, val=5)
