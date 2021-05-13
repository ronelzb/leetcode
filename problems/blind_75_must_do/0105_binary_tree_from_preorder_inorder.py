# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map_inorder = dict()
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        root = None
        stack = deque()
        for val in preorder:
            current = TreeNode(val)

            if root is None:
                root = current
            else:
                if map_inorder[val] < map_inorder[stack[-1].val]:
                    stack[-1].left = current
                else:
                    while stack and map_inorder[val] > map_inorder[stack[-1].val]:
                        last_popped = stack.pop()
                    last_popped.right = current

            stack.append(current)

        return root

    def build_tree_recursive(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map_inorder = dict()
        for i, val in enumerate(inorder):
            map_inorder[val] = i
        preorder_iter = iter(preorder)

        def recursion(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            preorder_val = next(preorder_iter)
            node = TreeNode(preorder_val)
            inorder_index = map_inorder[preorder_val]
            node.left = recursion(start, inorder_index - 1)
            node.right = recursion(inorder_index + 1, end)
            return node

        return recursion(0, len(preorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    sol.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
