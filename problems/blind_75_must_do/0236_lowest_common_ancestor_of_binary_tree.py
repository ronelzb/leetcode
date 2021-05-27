# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(3)

    t.left = TreeNode(5)
    t.left.left = TreeNode(6)
    t.left.right = TreeNode(2)
    t.left.right.left = TreeNode(7)
    t.left.right.right = TreeNode(4)

    t.right = TreeNode(1)
    t.right.left = TreeNode(0)
    t.right.right = TreeNode(8)

    print(sol.lowestCommonAncestor(t, t.left.right.left, t.right.right))
