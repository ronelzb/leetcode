# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# tags: #blind_75_must_do, #bst, #dfs
#
# Solution: DFS
# * Base recursion case: if root is None or is equal to one of the nodes to search
# * Traverse the tree from the root node
# * If both children are in tree then root is the ancestor of both, else return the one that is not None
# Time complexity: O(n), Space complexity: O(n)
from typing import Optional

from utils.tree_traversal_helper import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if not root or root == p or root == q:
            return root

        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    sol = Solution()

    bst = TreeNode(6,
                   TreeNode(2,
                            TreeNode(0,
                                     TreeNode(3),
                                     TreeNode(5)),
                            TreeNode(4)),
                   TreeNode(8,
                            TreeNode(7),
                            TreeNode(9)))

    print(sol.lowestCommonAncestor(bst, bst.left, bst.left.right))  # 2
