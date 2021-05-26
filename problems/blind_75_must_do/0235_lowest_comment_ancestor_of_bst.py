# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)
        node = root

        while not min_val <= node.val <= max_val:
            if node.val > min_val:
                node = node.left
            else:
                node = node.right

        return node


if __name__ == "__main__":
    sol = Solution()

    bst = TreeNode(6)

    bst.left = TreeNode(2)
    bst.left.left = TreeNode(0)
    bst.left.right = TreeNode(4)
    bst.left.left.left = TreeNode(3)
    bst.left.left.right = TreeNode(5)

    bst.right = TreeNode(8)
    bst.right.left = TreeNode(7)
    bst.right.right = TreeNode(9)

    print(sol.lowestCommonAncestor(bst, bst.left, bst.left.right))
