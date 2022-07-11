# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# tags: #binary_tree, #facebook, #hash_table
#
# Solution 1: DFS
# The important trick here is to find a way to keep the col indexes in order
# # We can achieve this keeping a dictionary with the col index (x_index)
# # and after traversing the tree sort the map by index
# # We also need to be careful on how to store those values in the same col-row index
# # For that, we will store a tuple with the row index when traversing the tree
# Time complexity: O((h*log(h))^2), Space complexity O(n)
#
# Solution 2: BFS
# Similar to DFS we will keep a col index variable
# There is an optimisation here to avoid sorting the dictionary at the end
# We use min_column and max_column to determine the range intervals
# As in any BFS we will use a queue to traverse the tree
# Time complexity: O(w*h*log(h)), Space complexity O(n)
from collections import deque, defaultdict
from typing import Optional, List

from utils.tree_traversal_helper import TreeNode


class Solution:
    def verticalOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        indexed_map = {}

        def dfs(current: Optional[TreeNode], x_index, y_index):
            if not current:
                return

            if x_index not in indexed_map:
                indexed_map[x_index] = []
            indexed_map[x_index].append((y_index, current.val))

            dfs(current.left, x_index - 1, y_index + 1)
            dfs(current.right, x_index + 1, y_index + 1)

        dfs(root, 0, 0)

        nodes = []
        for index in sorted(indexed_map):
            nodes.append([v for i, v in sorted(indexed_map[index], key=lambda x:x[0])])

        return nodes

    def verticalOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(0, root)])
        indexed_map = defaultdict(list)
        min_col, max_col = 0, 0

        while queue:
            col, node = queue.popleft()

            indexed_map[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((col - 1, node.left))
            if node.right:
                queue.append((col + 1, node.right))

        nodes = []
        for col in range(min_col, max_col + 1):
            nodes.append(indexed_map[col])

        return [indexed_map[col] for col in range(min_col, max_col + 1)]


if __name__ == '__main__':
    sol = Solution()

    t = TreeNode(3,
                 TreeNode(9),
                 TreeNode(20,
                          TreeNode(15),
                          TreeNode(7)))
    print(sol.verticalOrder_dfs(t))  # [[9],[3,15],[20],[7]]

    t = TreeNode(3,
                 TreeNode(9,
                          TreeNode(4),
                          TreeNode(0,
                                   TreeNode(5),
                                   None)),
                 TreeNode(8,
                          TreeNode(1,
                                   None,
                                   TreeNode(2)),
                          TreeNode(7)))
    print(sol.verticalOrder_dfs(t))  # [[4],[9,5],[3,0,1],[8,2],[7]]
