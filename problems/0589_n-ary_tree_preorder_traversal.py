# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None

        preorder_list = [root.val]
        children = root.children if root.children else []
        for child in children:
            preorder_list += self.preorder(child)

        return preorder_list


    def preorder_iterative(self, root: 'None') -> List[int]:
        queue = deque()
        preorder_list = []

        if root:
            queue.append(root)

        while queue:
            current = queue.popleft()
            preorder_list.append(current.val)

            if current.children:
                queue.extendleft(reversed(current.children))

        return preorder_list


if __name__ == "__main__":
    sol = Solution()

    tree1 = Node(1)
    tree1.children = [Node(3), Node(2), Node(4)]
    tree1.children[0].children = [Node(5), Node(6)]
    assert sol.preorder(tree1) == [1, 3, 5, 6, 2, 4]

    assert sol.preorder_iterative(tree1) == [1, 3, 5, 6, 2, 4]
