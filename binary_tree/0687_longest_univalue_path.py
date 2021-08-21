# https://leetcode.com/problems/longest-univalue-path/
# tags: #binary_tree, #dfs, #google, #tree
# The idea here is to find the longest "path" which we can connect edges with the same node value
# To achieve this we can post-traverse this tree finding the local max_left and max_right
# if node.left == node then we can say the edges connect otherwise we interrupt the count when
# we recurse back the tree.
# To get the global max_value we can set up a variable outside the boundaries of the dfs
# and compare the local max with global.
# dfs will return the max(max_left, max_right) to keep a "max path" when going back up the tree.
# Time complexity: O(n), Space complexity: O(n) it should be O(h) BUT worst case scenario is to have a skewed tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            nonlocal max_path

            max_left = dfs(node.left)
            max_left = max_left + 1 if node.left and node.left.val == node.val else 0
            max_right = dfs(node.right)
            max_right = max_right + 1 if node.right and node.right.val == node.val else 0

            max_path = max(max_path, max_left + max_right)

            return max(max_left, max_right)

        dfs(root)
        return max_path


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(1)
    t.left = TreeNode(4)
    t.right = TreeNode(5)

    t.left.left = TreeNode(4)
    t.left.right = TreeNode(4)

    t.right.right = TreeNode(5)

    print(sol.longestUnivaluePath(t))  # 2

