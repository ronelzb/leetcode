# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# tags: #bst, #dfs, #sorting, #stack
#
# Solution 1: Stack
# Traverse both bst like we normally do using stacks to simulate in-order traversal
# To merge the stack values, we will compare them:
# * If stack1[-1] <= stack2[-1] then get stack1 value and move roo1 to the right side of its current node
# * Else, get stack2 and move root2 node to the right
# Time complexity: O(r1 + r2), Space complexity O(h1 + h2)
#
# Solution 2: In-order traversal (DFS)
# Traverse each tree, using inorder traversal
# Merge the resulting list using the same logic as merge sort
# Time complexity: O(r1 + r2), Space complexity O(h1 + h2)
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = deque(), deque()
        res = []

        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if len(stack2) == 0 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                res.append(root2.val)
                root2 = root2.right

        return res

    def getAllElements_inorder(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root: TreeNode, lst: List[int]) -> None:
            if root is None: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)

        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)

        res = []
        i1, i2 = 0, 0
        len1, len2 = len(list1), len(list2)

        while i1 < len1 and i2 < len2:
            if list1[i1] <= list2[i2]:
                res.append(list1[i1])
                i1 += 1
            else:
                res.append(list2[i2])
                i2 += 1

        return res + list1[i1:] + list2[i2:]


if __name__ == "__main__":
    sol = Solution()

    r1 = TreeNode(2)
    r1.left = TreeNode(1)
    r1.right = TreeNode(4)

    r2 = TreeNode(1)
    r2.left = TreeNode(0)
    r2.right = TreeNode(3)
    print(sol.getAllElements_inorder(r1, r2))  # [0,1,1,2,3,4]
