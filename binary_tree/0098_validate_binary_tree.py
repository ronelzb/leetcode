# https://leetcode.com/problems/validate-binary-search-tree/
# tags: #binary_tree, #bst, #dfs
#
# Solution: DFS
# Recursively iterating over the tree while defining interval <min_val, max_val> for each node.
# Time complexity: O(n), Space complexity: O(n)
import sys
from typing import Optional

from utils.tree_traversal_helper import TreeNode


class Solution:
    def isValidBST(
            self,
            root: Optional[TreeNode],
            min_val: int = -(sys.maxsize - 1),
            max_val: int = sys.maxsize
    ) -> bool:
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return (self.isValidBST(root.left, min_val, root.val)
                and self.isValidBST(root.right, root.val, max_val))


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(2,
                 TreeNode(1),
                 TreeNode(3))
    print(sol.isValidBST(t))  # True

    t = TreeNode(0,
                 None,
                 TreeNode(-1))
    print(sol.isValidBST(t))  # False
