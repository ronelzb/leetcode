# https://leetcode.com/problems/binary-tree-inorder-traversal/
# tags: #binary_tree, #dfs, #stack, #top_interview_questions, #tree
#
# Both solutions use dfs for traversal
# First solution is recursive, second is iterative using stack
#
# Time complexity: O(n), Space complexity: O(n)
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal_Stack(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = deque()
        current = root

        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    print(sol.inorderTraversal(t))  # [1, 3, 2]
    print(sol.inorderTraversal_Stack(t))  # [1, 3, 2]
