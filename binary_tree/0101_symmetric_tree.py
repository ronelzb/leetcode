# https://leetcode.com/problems/symmetric-tree/
# tags: #bfs, #binary_tree, #dfs
#
# Solution: DFS (Recursion)
# In the dfs approach check if the tree is well-formed,
# when doing the recursion shuffle left side to left and right side to right and vice versa.
# Time complexity: O(n), Space complexity O(h)
#
# Solution: Stack (Iterative)
# Use a stack to simulate the recursion done in Solution 1
# Time complexity: O(n), Space complexity O(h)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def isSymmetric_dfs(self, root: Optional[TreeNode]) -> bool:
        def symmetric_helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return symmetric_helper(left.left, right.right) and \
                   symmetric_helper(left.right, right.left)

        return symmetric_helper(root.left, root.right)

    def isSymmetric_iter(self, root: Optional[TreeNode]) -> bool:
        stack = deque([(root.left, root.right)])

        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


if __name__ == "__main__":
    sol = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(4)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(4)
    t1.right.right = TreeNode(3)
    print(sol.isSymmetric_iter(t1))  # True

    t2 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left.right = TreeNode(3)
    t1.right = TreeNode(2)
    t1.right.right = TreeNode(3)
    print(sol.isSymmetric_iter(t1))  # False

    t3 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    print(sol.isSymmetric_iter(t1))  # False
