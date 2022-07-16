# https://leetcode.com/problems/max-area-of-island/
# tags: #bfs, #binary_tree, #dfs, #google
#
# Solution: LCA + find path (DFS)
# The first important trick on this solution is to find the lowest common ancestor (LCA) because:
# * It will narrow down the path search between start and end values
# The second part is to start at lca and find the path to both values to save time.
# Time complexity : O(n), Space complexity: O(n)
from collections import deque
from typing import Optional

from utils.tree_traversal_helper import TreeNode


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)

            if left and right:
                return node
            return left or right

        root = lca(root)

        def find_path(node, val, path):
            if node.val == val:
                return True
            if node.left and find_path(node.left, val, path):
                path += "L"
            elif node.right and find_path(node.right, val, path):
                path += "R"
            return True if path else False

        path_to_start, path_to_destination = [], []
        find_path(root, startValue, path_to_start)
        find_path(root, destValue, path_to_destination)

        return "U" * len(path_to_start) + "".join(reversed(path_to_destination))


if __name__ == '__main__':
    sol = Solution()

    t = TreeNode(5,
                 TreeNode(1,
                          TreeNode(3),
                          None),
                 TreeNode(2,
                          TreeNode(6),
                          TreeNode(4)))
    print(sol.getDirections(root=t, startValue=3, destValue=6))  # "UURL"
