# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# tags: #bfs, #binary_tree, #divide_and_conquer
#
# This problem can have multiple solution approaches, my solution uses a queue and reverse insert
# for each level instead of list.
#
# Time complexity: O(n), Space complexity: O(n)
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        tree_list = []
        tree_list_len = 0
        queue = deque([(1, root)])

        while queue:
            level, node = queue.popleft()

            if level > tree_list_len:
                tree_list.append([])
                tree_list_len += 1
            if level % 2 != 0:
                tree_list[level - 1].append(node.val)
            else:
                tree_list[level - 1].insert(0, node.val)

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        return tree_list


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print(sol.zigzagLevelOrder(t))  # [[3],[20,9],[15,7]]
