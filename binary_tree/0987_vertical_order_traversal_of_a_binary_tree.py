# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# tags: #dfs, #bfs, #bst, #facebook, #hash_table
#
# Solution: BFS using Queue + Sort at each level/column
# Starting on the premise of using a queue to traverse the BST using BFS, at level row find all nodes over that level
# Store all nodes in a temporary dictionary split by column, when storing the result nodes back to our global
# dictionary sort the result at each given column, this will ensure to have all nodes in the same col/row sorted.
# Time complexity: O(n*log(n)), Space complexity O(n)
import bisect
from collections import deque, defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols_list = defaultdict(list)
        queue = deque([(root, 0)])
        min_col, max_col = 0, 0

        while queue:
            aux = defaultdict(list)
            for _ in range(len(queue)):
                node, col = queue.popleft()
                aux[col].append(node.val)

                if node.left:
                    queue.append((node.left, col - 1))
                    min_col = min(min_col, col - 1)
                if node.right:
                    queue.append((node.right, col + 1))
                    max_col = max(max_col, col + 1)

            for i in aux:
                cols_list[i].extend(sorted(aux[i]))

        return [cols_list[i] for i in range(min_col, max_col + 1)]


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(3)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)
    print(sol.verticalTraversal(r))  # [[9],[3,15],[20],[7]]

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(6)
    r.right = TreeNode(3)
    r.right.left = TreeNode(5)
    r.right.right = TreeNode(7)
    print(sol.verticalTraversal(r))  # [[4],[2],[1,5,6],[3],[7]]
