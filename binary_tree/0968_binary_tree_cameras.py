# https://leetcode.com/problems/binary-tree-cameras/://leetcode.com/problems/longest-palindromic-substring/
# tags: #dfs, #dp, #binary_tree
#
# Solution: Depth-first search
# Each leaf node has only one of two ways it can be monitored:
# 1. Place a camera on the leaf node.
# 2. Place a camera on the parent node of the leaf node.
# We can use different values to assign meaning to the nodes:
# * Find unmonitored child nodes (which are left as 0s) -> the current (parent) node has to have a camera.
# * Find child nodes with cameras -> the current (parent) node is monitored.
# * Otherwise, the current node is unmonitored, treat as leaf node.
# Time complexity: O(n), Space complexity: O(h)
from typing import Optional

from utils.tree_traversal_helper import TreeNode


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            res = dfs(node.left) + dfs(node.right)
            curr = 2
            if node.left and node.right:
                curr = min(node.left.val, node.right.val)
            elif node.left or node.right:
                curr = node.left.val if node.left else node.right.val

            if curr == 0:
                node.val = 1
                res += 1
            elif curr == 1:
                node.val = 2

            return res

        return dfs(root) + (root.val == 0)


if __name__ == '__main__':
    sol = Solution()

    print(sol.minCameraCover(TreeNode(0,
                                      TreeNode(0,
                                               TreeNode(0,
                                                        TreeNode(None, TreeNode(0)))))))  # 2
