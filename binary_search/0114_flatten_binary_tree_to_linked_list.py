# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# tags: #binary_tree, #dfs, #linked_list, #stack
#
# Solution 1: DFS
# Preorder traversal using recursion. For this problem, we use TreeNode prev to hold the next node.
# After flatten(root.right), we have processed the right branch of the current node,
# and the current prev is the head of root of the right branch.
# For now, we want to know which node is the precedent node of prev, and we will set this particular node's
# next attribute as prev. As per the problem, this particular node is actually the rightmost node of the left branch.
# Next, let's say why we can actually get it. So now we go to the next line, which is flatten(root.left).
# When we go deeper and deeper in the recursion, we are actually going right because we go right before we go left.
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: Stack
# Same idea as solution 1 but using Stack, graphical explanation:
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36991/Accepted-simple-Java-solution-iterative/576062
# Time complexity: O(n), Space complexity O(n)
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
    def __init__(self):
        self.prev = None

    def flatten_dfs(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return

        self.flatten_dfs(root.right)
        self.flatten_dfs(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

    def flatten_stack(self, root: Optional[TreeNode]) -> None:
        if root is None: return None

        stack = deque([root])
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
            node.left = None


if __name__ == "__main__":
    sol = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(4)

    t1.right = TreeNode(5)
    t1.right.right = TreeNode(6)
    sol.flatten_stack(t1)

    c = t1
    while c:
        print(c, end=" -> ")
        c = c.right
    print("", end="\n")
