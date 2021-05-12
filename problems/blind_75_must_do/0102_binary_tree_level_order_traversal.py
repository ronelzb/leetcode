# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        q = deque([(root, 1)])
        max_level = 0
        result = []

        while q:
            current, level = q.popleft()
            if level > max_level:
                result.append([])
                max_level = level

            result[level - 1].append(current.val)

            if current.left:
                q.append((current.left, level + 1))
            if current.right:
                q.append((current.right, level + 1))

        return result


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    assert sol.levelOrder(t) == [[3], [9, 20], [15, 7]]
