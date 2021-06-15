# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.right is None:
            return self.minDepth(root.left) + 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print(sol.minDepth(t))  # 2
