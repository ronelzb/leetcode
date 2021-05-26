# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        bst_list = []

        def bst_to_list(node: TreeNode) -> None:
            if node is None:
                return

            bst_to_list(node.left)
            bst_list.append(node.val)
            bst_to_list(node.right)

        bst_to_list(root)
        print(bst_list)

        return bst_list[k - 1]

    def kthSmallest_iterative(self, root: TreeNode, k: int) -> int:
        stack = deque()
        node = root
        left_count = 0

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                left_count += 1

                if left_count == k:
                    return node.val
                node = node.right


if __name__ == "__main__":
    sol = Solution()

    bst = TreeNode(5)

    bst.left = TreeNode(3)
    bst.left.left = TreeNode(2)
    bst.left.right = TreeNode(4)
    bst.left.left.left = TreeNode(1)

    bst.right = TreeNode(6)

    print(sol.kthSmallest_iterative(bst, 3))
