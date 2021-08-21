# https://leetcode.com/problems/range-sum-of-bst/
# tags: #binary_tree, #dfs, #google, #tree
# The solution here is dfs through the entire bst checking that the current node is between [low, high]
# An improvement to the initial dfs is to verify that the current node is inside either low or high
# To continue going down the tree
# Time complexity: O(n), Space complexity: O(n) it should be O(h) BUT worst case scenario is to have a skewed tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        sum_path = root.val if low <= root.val <= high else 0

        if root.val > low and root.left:
            sum_path += self.rangeSumBST(root.left, low, high)

        if root.val < high and root.right:
            sum_path += self.rangeSumBST(root.right, low, high)

        return sum_path


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(15)

    t.left.left = TreeNode(3)
    t.left.right = TreeNode(7)

    t.right.right = TreeNode(15)
    t.right.right = TreeNode(18)

    print(sol.rangeSumBST(t, low=7, high=15))  # 32
