# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# tags: #dfs
#
# Solution: Depth First Search
# We recursively pass the current value of path to the children.
# At each node calculate the new sum multiplying the current value by 2 and then adding node.val
# Find the sum of both left and right children
# Time complexity: O(n), Space complexity O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node: return 0
            current_sum = (current_sum << 1) + node.val
            if node.left is None and node.right is None:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(1)
    r.left = TreeNode(0)
    r.left.left = TreeNode(0)
    r.left.right = TreeNode(1)

    r.right = TreeNode(1)
    r.right.left = TreeNode(0)
    r.right.right = TreeNode(1)
    print(sol.sumRootToLeaf(r))  # 22

    r = TreeNode(0)
    print(sol.sumRootToLeaf(r))  # 0

    r = TreeNode(1)
    r.left = TreeNode(1)
    print(sol.sumRootToLeaf(r))  # 3
