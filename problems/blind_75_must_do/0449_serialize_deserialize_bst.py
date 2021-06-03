# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        output = []
        node = root
        stack = deque()

        while node or stack:
            if node:
                output.append(str(node.val) + ",")
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        return "".join(output)

    def deserialize(self, data: str) -> TreeNode:
        tree_list = data.split(",")
        tree_list.pop()
        stack = deque()
        root = None

        for num in tree_list:
            num = int(num)
            if not root:
                root = TreeNode(num)
                stack.append(root)
            else:
                node = TreeNode(num)
                if num < stack[-1].val:
                    stack[-1].left = node
                else:
                    while stack and num > stack[-1].val:
                        u = stack.pop()
                    u.right = node
                stack.append(node)

        return root


if __name__ == "__main__":
    c = Codec()

    # bst = TreeNode(9)
    # bst.left = TreeNode(3)
    # bst.right = TreeNode(20)
    # bst.right.left = TreeNode(15)
    # bst.right.right = TreeNode(25)

    bst = TreeNode(None)

    ser = c.serialize(bst)
    print(ser)
    bst = c.deserialize(ser)
