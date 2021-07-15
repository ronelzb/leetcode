# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    # Solution steps:
    # 1. Loop through level 0 to level n - 2
    # 2. Traverse this level and connect children.
    # As we're traversing the children we join right child with current.next left child if it exists
    # Time complexity: 0(n), Space complexity O(1)
    def connect(self, root: 'Node') -> 'Node':
        prev = root
        while prev is not None and prev.left is not None:
            current = prev
            while current is not None:
                current.left.next = current.right
                current.right.next = current.next.left if current.next else None
                current = current.next

            prev = prev.left

        return root


if __name__ == "__main__":
    sol = Solution()

    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.right.left = Node(6)
    t.right.right = Node(7)

    sol.connect(t)
