# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


def pre_order_traversal(current: TreeNode, lvl=0):
    if current is None:
        return

    indent = " " * lvl * 2
    output = f"{current.val}\n"

    if current.left:
        output += f"{indent}L:"
        output += pre_order_traversal(current.left, lvl + 1)
    if current.right:
        output += f"{indent}R:"
        output += pre_order_traversal(current.right, lvl + 1)

    return output


if __name__ == "__main__":
    r = TreeNode(4)
    r.left = TreeNode(2)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(3)

    r.right = TreeNode(7)
    r.right.left = TreeNode(6)
    r.right.right = TreeNode(9)

    sol = Solution()
    print(pre_order_traversal(r))
    sol.invertTree(r)
    print(pre_order_traversal(r))