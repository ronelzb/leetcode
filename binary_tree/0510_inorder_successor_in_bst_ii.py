# https://leetcode.com/problems/gas-station/
# tags: #bst
#
# Solution: Successor and predecessor
# * If the node has a right child, then inorder successor is the left-most child in its right subtree.
# This is because successor is greater than self but also immediately after.
# * Else, successor is somewhere up the parent chain, since it can't be in left subtree (if at all there).
# Keep traversing up the parent chain till you find a node that is the left child of its parent. This is the successor
# Time complexity: O(h), Space complexity O(1)
from typing import Optional
from utils.tree_traversal_helper import Node


class Solution:
    def inorderSuccessor(self, node: Node) -> Optional[Node]:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent


if __name__ == '__main__':
    sol = Solution()

    t = Node(2,
             Node(1),
             Node(3))
    print(sol.inorderSuccessor(t.left))  # 2

    t = Node(5,
             Node(3,
                  Node(2,
                       Node(1)),
                  Node(4)),
             Node(6))
    print(sol.inorderSuccessor(t.right))  # None
