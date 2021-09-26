# https://leetcode.com/problems/same-tree/
# tags: #binary_tree, #dfs, #microsoft
#
# Solution: DFS
# * Equal nullity denotes that this branch is the same (local equality)
# * Unequal nullity denotes that the trees aren't the same
# * Both nodes have values, descend if those values are equal
# Time complexity: O(n) n=len(p), Space complexity: O(n)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()

    p_root = TreeNode(1)
    p_root.left = TreeNode(2)
    p_root.right = TreeNode(3)

    q_root = TreeNode(1)
    q_root.left = TreeNode(2)
    q_root.right = TreeNode(3)

    assert sol.isSameTree(p_root, q_root)
