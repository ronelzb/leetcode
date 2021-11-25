# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Tags: #dp, #binary_tree, #dfs
#
# Solution: Recursion stack
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
# Time complexity: O(n), Space complexity: O(n).
import sys


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_path = -(sys.maxsize - 1)

    def maxPathSum(self, root: TreeNode) -> int:
        def get_max(node: TreeNode) -> int:
            if node is None:
                return 0

            gain_left = max(get_max(node.left), 0)
            gain_right = max(get_max(node.right), 0)

            # going down the stack the maximum path we can form is
            # the node itself
            # max gain from left
            # max gain from right
            # It is important to understand the different between looking for the maximum path INVOLVING
            # the current node in process and what we return for the node which starts the recursion stack
            current_max = node.val + gain_left + gain_right
            self.max_path = max(current_max, self.max_path)

            # going up the stack we can only form a path involving the parent
            # and only one of the branches
            return node.val + max(gain_left, gain_right)

        get_max(root)
        return self.max_path


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    print(sol.maxPathSum(t))  # 6
