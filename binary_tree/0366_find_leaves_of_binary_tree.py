# https://leetcode.com/problems/find-leaves-of-binary-tree/
# tags: #binary_tree, #dfs, #google
#
# Solution: DFS
# In this solution let's make a dfs variant: You can directly append the leaves in a list and
# add the lists as you go from bottom to top chopping the leaves as we traverse the tree
# Time complexity : O(h * log(n)), Space complexity: O(n)
from typing import List, Optional

from utils.tree_traversal_helper import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode]) -> (Optional[TreeNode], List[int]):
            if not node:
                return None, []
            if not node.left and not node.right:
                return None, [node.val]

            node.left, left_leaves = dfs(node.left)
            node.right, right_leaves = dfs(node.right)
            return node, left_leaves + right_leaves

        nodes = []
        while root:
            root, leaves = dfs(root)
            nodes.append(leaves)

        return nodes


if __name__ == '__main__':
    sol = Solution()

    t = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3))
    print(sol.findLeaves(root=t))  # [[4,5,3],[2],[1]]
