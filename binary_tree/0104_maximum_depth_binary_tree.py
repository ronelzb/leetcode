# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# tags: #binary_tree, #dfs, #microsoft
#
# Solution: Depth-first search
# Classical DFS problem, use recursion incrementing the level at each call, compare the max between children
# Time complexity: O(n), Space complexity: (n)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode, level: int = 0) -> int:
        if root is None:
            return level

        return max(self.maxDepth(root.left, level + 1), self.maxDepth(root.right, level + 1))


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    assert sol.maxDepth(t) == 3
