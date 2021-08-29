# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# tags: #bfs, #binary_tree, #design, #dfs, #google, #string
#
# Amazing solution explanation:
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
#
# When serializing and deserializing we need to be consistent in the traversal we choose to make.
# In this case, I used preorder traversal taking care of the base case marking as "null" empty nodes.
#
# Deserialization uses an iter helper to efficiently keep the current position we are traversing.
# Take care of the base case (current == "null") and return a node in which its children will be retrieved
# recursively.
#
# Time complexity: O(n), Space complexity: O(n)
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_helper() -> TreeNode:
            current = next(values)
            if current == "null":
                return None
            node = TreeNode(int(current))
            node.left = deserialize_helper()
            node.right = deserialize_helper()
            return node

        values = iter(data.split(","))
        return deserialize_helper()


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.right.left = TreeNode(4)
    t.right.right = TreeNode(5)

    c = Codec()
    serialized = c.serialize(t)
    print(serialized)  # [1,2,null,null,3,4,null,null,5,null,null]

    deserialized = c.deserialize(serialized)
