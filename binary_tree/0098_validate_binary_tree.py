# https://leetcode.com/problems/validate-binary-search-tree/
# tags: #binary_tree, #bst, #dfs
#
# Solution: DFS
# Recursively iterating over the tree while defining interval <min_val, max_val> for each node.
# Time complexity: O(n), Space complexity: O(n)
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, min_val: int = None, max_val: int = None) -> bool:
        if root is None:
            return True

        if (min_val is not None and root.val <= min_val) or (max_val is not None and root.val >= max_val):
            return False

        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)


if __name__ == "__main__":
    sol = Solution()

    # tree_root = TreeNode(2)
    # tree_root.left = TreeNode(1)
    # tree_root.right = TreeNode(3)
    #
    # assert sol.isValidBST(tree_root)

    tree_root = TreeNode(0)
    tree_root.right = TreeNode(-1)

    assert not sol.isValidBST(tree_root)
