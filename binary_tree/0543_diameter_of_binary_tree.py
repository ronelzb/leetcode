# https://leetcode.com/problems/diameter-of-binary-tree/
# tags: #binary_tree, #dfs, #google
#
# Solution 1: Max Depth + Global variable
# Max Depth recursion variant:
# The longest path that passes a given node as the ROOT node is T = left_height + right_height.
# So you just calculate T for all nodes and output the max T.
# Time Complexity: O(n), Space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_max(node: TreeNode) -> int:
            if node is None:
                return 0

            max_left = get_max(node.left)
            max_right = get_max(node.right)
            self.max_length = max(self.max_length, max_left + max_right)

            return max(max_left, max_right) + 1

        get_max(root)
        return self.max_length


if __name__ == "__main__":
    h = TreeNode(1)
    h.left = TreeNode(2)
    h.left.left = TreeNode(4)
    h.left.right = TreeNode(5)

    h.right = TreeNode(3)

    sol = Solution()
    print(sol.diameterOfBinaryTree(h))  # 3

    h = TreeNode(1)
    h.left = TreeNode(2)

    sol = Solution()
    print(sol.diameterOfBinaryTree(h))  # 1
