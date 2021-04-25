# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

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
    sol = Solution()

    tree1 = TreeNode(3)
    tree1.left = TreeNode(0)
    tree1.right = TreeNode(4)
    tree1.left.right = TreeNode(2)
    tree1.left.right.left = TreeNode(1)
    print(pre_order_traversal(tree1))

    trimmed_tree = sol.trimBST(tree1, 1, 3)
    print(pre_order_traversal(trimmed_tree))
