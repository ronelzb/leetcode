# https://leetcode.com/problems/binary-search-tree-iterator/
# tags: #bst, #iterator, #stack
#
# Solution: DFS + stack
# At init time build a stack that will be a list based on bst in-order traversal
# Then, for next method pop the first element in the list and hasNext method check if stack has any elements left
# Time complexity: O(n), Space complexity O(n)
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def build_stack(node: Optional[TreeNode]) -> List[int]:
            if node is None: return []
            return build_stack(node.left) + [node.val] + build_stack(node.right)

        self.stack = build_stack(root)

    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == "__main__":
    t1 = TreeNode(7)
    t1.left = TreeNode(3)
    t1.right = TreeNode(15)
    t1.right.left = TreeNode(9)
    t1.right.right = TreeNode(20)

    bst_iter = BSTIterator(t1)
    print(bst_iter.next())  # 3
    print(bst_iter.next())  # 7
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 9
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 15
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 20
    print(bst_iter.hasNext())  # False
