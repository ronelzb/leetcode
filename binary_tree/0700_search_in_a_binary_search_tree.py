# https://leetcode.com/problems/search-in-a-binary-search-tree/
# tags: #bst
#
# Solution: Recursion
# Classical Binary Search Tree (bst) traversal knowing that: the left subtree is always lesser than root and
# right subtree is always bigger than root.
# Time complexity: O(h), Space complexity O(h)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return None

        if root.val == val: return root
        return self.searchBST(root.left if root.val > val else root.right, val)


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(4)
    r.left = TreeNode(2)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(3)
    r.right = TreeNode(7)
    node = sol.searchBST(r, 2)
    print(node.val if node else None)  # 2
