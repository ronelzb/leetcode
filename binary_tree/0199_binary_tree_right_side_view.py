# https://leetcode.com/problems/binary-tree-right-side-view/
# tags: #bfs, #dfs
#
# Solution 1: DFS
# Make a pre-order traversal from right to left keeping track of the max level
# At each recursion call if level is greater than max_level it means we found a new visible node from the right
# and every we go deeper max_level += len of the current list
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: BFS
# Similar to the DFS solution but using a queue
# Time complexity: O(n), Space complexity O(n)
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView_dfs(self, root: Optional[TreeNode], level: int = 0, max_level: int = -1) -> List[int]:
        if root is None: return []

        right_view = []
        if level > max_level:
            right_view.append(root.val)

        right_view.extend(self.rightSideView_dfs(root.right, level + 1, max_level + len(right_view)))
        right_view.extend(self.rightSideView_dfs(root.left, level + 1, max_level + len(right_view)))

        return right_view

    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        max_level = -1
        queue = deque([(0, root)])
        right_view = []

        while queue:
            level, node = queue.popleft()

            if level > max_level:
                right_view.append(node.val)
                max_level = level
            if node.right:
                queue.append((level + 1, node.right))
            if node.left:
                queue.append((level + 1, node.left))

        return right_view


if __name__ == "__main__":
    sol = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left = TreeNode(5)

    t1.right = TreeNode(3)
    t1.right.left = TreeNode(6)
    t1.right.left.left = TreeNode(7)
    t1.right.right = TreeNode(4)
    print(sol.rightSideView_bfs(t1))  # [1,3,4,7]

    t1 = TreeNode(1)
    t1.right = TreeNode(3)
    print(sol.rightSideView_bfs(t1))  # [1,3]
