# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# tags: #array, #hash_table, #divide_and_conquer
#
# Solution: Recursion (Divide and conquer)
# Use post order to recursively insert elements using preorder traversal
# Inorder is used as a base case for the recursion cutting the input array in half at each recursion call
# Time complexity: O(n^2), Space complexity O(n^2)
#
# Solution optimized: Recursion (Divide and conquer)
# Same overall solution as the previous one
# In this case initialize a num to index dictionary and half the inorder array using this dictionary
# Time complexity: O(n), Space complexity O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder: return None

        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root

    def buildTree_optimized(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree_helper(low: int, high: int) -> Optional[TreeNode]:
            if low > high: return None
            node = TreeNode(postorder.pop())
            middle = inorder_dict[node.val]

            node.right = buildTree_helper(middle + 1, high)
            node.left = buildTree_helper(low, middle - 1)
            return node

        inorder_dict = {num: i for i, num in enumerate(inorder)}
        return buildTree_helper(0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    t1 = sol.buildTree_optimized(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
