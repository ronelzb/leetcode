# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def match_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if (not s and t) or (s and not t):
            return False

        if not s and not t:
            return True

        if s.val != t.val:
            return False

        return self.match_subtree(s.left, t.left) and self.match_subtree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        mst = self.match_subtree(s, t) if s.val == t.val else False

        return mst or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == "__main__":
    sol = Solution()
    root_s = TreeNode(3)
    root_s.left = TreeNode(4)
    root_s.right = TreeNode(5)
    root_s.left.left = TreeNode(1)
    root_s.left.right = TreeNode(2)

    root_t = TreeNode(4)
    root_t.left = TreeNode(1)
    root_t.right = TreeNode(2)

    assert sol.isSubtree(root_s, root_t)

    root_s.left.right.left = TreeNode(0)

    assert not sol.isSubtree(root_s, root_t)
