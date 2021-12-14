# https://leetcode.com/problems/binary-search-tree-iterator/
# tags: #bst, #facebook, #iterator, #stack
#
# Solution: DFS + stack
# At init time build a stack that will be a list based on bst in-order traversal
# Then, for next method pop the first element in the list and hasNext method check if stack has any elements left
# Time complexity: O(n), Space complexity O(n)
#
# Solution Followup: Generator
# This solution is based on skipping the stack part using a generator with Python built-in yield.
# Time complexity: O(n), Space complexity O(h)
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


class BSTIteratorGenerator:
    def __init__(self, root: Optional[TreeNode]):
        self.current = None
        self.last = root
        self.iter = self.iterate(root)

        while self.last and self.last.right:
            self.last = self.last.right

    def hasNext(self):
        return self.current is not self.last

    def next(self):
        return next(self.iter)

    def iterate(self, node: Optional[TreeNode]):
        if node is None:
            return
        for x in self.iterate(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterate(node.right):
            yield x


if __name__ == "__main__":
    t1 = TreeNode(7)
    t1.left = TreeNode(3)
    t1.right = TreeNode(15)
    t1.right.left = TreeNode(9)
    t1.right.right = TreeNode(20)

    bst_iter = BSTIteratorGenerator(t1)
    print(bst_iter.next())  # 3
    print(bst_iter.next())  # 7
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 9
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 15
    print(bst_iter.hasNext())  # True
    print(bst_iter.next())  # 20
    print(bst_iter.hasNext())  # False
