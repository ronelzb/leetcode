# https://leetcode.com/problems/sum-of-left-leaves/
# tags: #bfs, #binary_tree, #dfs
#
# Solution: Depth-first search
# Preorder tree traversal in which we validate if the current node is not None and has children as the
# base case of the recursion, then check if the left children is a leaf and sum its value to the
# overall answer.
# Time complexity: O(n), Space complexity O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0

        left_leaves_sum = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                left_leaves_sum += root.left.val
            else:
                left_leaves_sum += self.sumOfLeftLeaves(root.left)

        left_leaves_sum += self.sumOfLeftLeaves(root.right)
        return left_leaves_sum


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(3)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)
    print(sol.sumOfLeftLeaves(r))  # 24

    r = TreeNode(1)
    r.left = TreeNode(2)
    print(sol.sumOfLeftLeaves(r))  # 2
