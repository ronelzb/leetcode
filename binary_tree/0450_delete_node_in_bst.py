# https://leetcode.com/problems/delete-node-in-a-bst/
# tags: #binary_tree, #bst, #google
#
# Solution: DFS
# Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned
# subtree
# Once the node is found, have to handle the below 4 cases:
# * Node doesn't have left or right - return null
# * Node only has left subtree- return the left subtree
# * Node only has right subtree- return the right subtree
# * Node has both left and right - find the minimum value in the right subtree,
# set that value to the currently found node, then recursively delete the minimum value in the right subtree
# Time complexity: O(h) => O(log(n)), Space complexity O(h)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return root

        if root.val == key:
            if root.left is None: return root.right
            elif root.right is None: return root.left

            min_right_descendant = root.right
            while min_right_descendant.left:
                min_right_descendant = min_right_descendant.left
            min_right_descendant.left = root.left
            return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


def traverse_preorder(node: Optional[TreeNode], level: int = 0) -> str:
    output = " " * level + str(node)

    if node.left:
        output += "\n" + traverse_preorder(node.left, level + 1)
    if node.right:
        output += "\n" + traverse_preorder(node.right, level + 1)

    return output


if __name__ == "__main__":
    sol = Solution()

    t1 = TreeNode(5)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(2)
    t1.left.right = TreeNode(4)
    t1.right = TreeNode(6)
    t1.right.right = TreeNode(7)
    t1 = sol.deleteNode(t1, 3)
    print(traverse_preorder(t1))
