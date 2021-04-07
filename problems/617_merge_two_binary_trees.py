# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node

        return root1 or root2


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

    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)
    print(pre_order_traversal(tree1))

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)
    print(pre_order_traversal(tree2))

    merged_tree = sol.mergeTrees(tree1, tree2)
    print(pre_order_traversal(merged_tree))

    tree1 = TreeNode(1)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    merged_tree = sol.mergeTrees(tree1, tree2)
    print(pre_order_traversal(merged_tree))
