# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# tags: #array, #binary_tree, #bst, #stack
#
# Solution 1: Recursion
# The first solution that usually comes to the mind is to use recursion
# Base case is when current node is None then we return the value instantiated
# Then, traverse the binary search tree left or right depending val is less or greater than the current node
# Time Complexity: O(n*log(n)), Space complexity: O(n)
#
# Solution 2: Recursion using Boundary
# Give the function a bound the maximum number it will handle.
# The left recursion will take the elements smaller than node.val
# The right recursion will take the remaining elements smaller than bound
# Time Complexity: O(n), Space complexity: O(n)
#
# Solution 3: Stack
# First item in preorder list is the root to be considered.
# For next item in preorder list, there are 2 cases to consider:
# * If value is less than last item in stack, it is the left child of last item.
# * If value is greater than last item in stack, pop it.
# The last popped item will be the parent and the item will be the right child of the parent.
# Time Complexity: O(n), Space complexity: O(n)
import sys
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def preorderInsert(node: TreeNode, val: int) -> TreeNode:
            if node is None:
                return TreeNode(val)

            if val < node.val:
                node.left = preorderInsert(node.left, val)
            else:
                node.right = preorderInsert(node.right, val)
            return node

        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            root = preorderInsert(root, preorder[i])

        return root

    def bstFromPreorder_Bound(self, preorder: List[int]) -> Optional[TreeNode]:
        def preorderInsert(sub_array, bound) -> TreeNode:
            if not sub_array or sub_array[-1] > bound: return None
            node = TreeNode(sub_array.pop())
            node.left = preorderInsert(sub_array, node.val)
            node.right = preorderInsert(sub_array, bound)
            return node

        return preorderInsert(preorder[::-1], sys.maxsize)

    def bstFromPreorder_Stack(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = deque([root])

        for num in preorder[1:]:
            if num < stack[-1].val:
                stack[-1].left = TreeNode(num)
                stack.append(stack[-1].left)
            else:
                last = None
                while stack and num > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(num)
                stack.append(last.right)

        return root


if __name__ == "__main__":
    sol = Solution()
    print(sol.bstFromPreorder_Bound(preorder=[8, 5, 1, 7, 10, 12]))  # [8,5,10,1,7,null,12]
