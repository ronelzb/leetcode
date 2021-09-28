# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# tags: #binary_tree, #divide_and_conquer, #hash_table
#
# Solution 1: Stack + dictionary
# * Keep pushing the nodes from the preorder into a stack (and keep making the tree by adding nodes to the left
# of the previous node) until the top of the stack matches the inorder.
# * At this point, pop the top of the stack until the top does not equal inorder
# (keep a flag to note that you have made a pop).
# * Repeat 1 and 2 until preorder is empty. The key point is that whenever the flag is set,
# insert a node to the right and reset the flag.
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 2: Recursion
# Explanation at:
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/981152/Recursion-or-Explanation-%2B-Visuals-or-Python
# Time complexity: O(n), Space complexity: O(n)
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
