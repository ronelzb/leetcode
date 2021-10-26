# https://leetcode.com/problems/invert-binary-tree/
# tags: #binary_tree, #bfs, #dfs, #microsoft
#
# Solution: Recursion DFS
# Time Complexity: O(n), Space complexity: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


def traverse_preorder(node: TreeNode, level: int = 0) -> str:
    output = " " * level + str(node)

    if node.left:
        output += "\n" + traverse_preorder(node.left, level + 1)
    if node.right:
        output += "\n" + traverse_preorder(node.right, level + 1)

    return output


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(4)
    t.left = TreeNode(2)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)

    t.right = TreeNode(7)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)

    print(traverse_preorder(t))

    t = sol.invertTree(t)
    print(traverse_preorder(t))
