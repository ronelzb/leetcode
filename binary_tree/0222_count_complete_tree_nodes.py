# https://leetcode.com/problems/count-complete-tree-nodes/
# tags: #binary_search, #binary_tree, #dfs
#
# Solution 1: Recursion into finding full binary tree
# The idea is to find whether a subtree is full binary tree or not.
# If it is then we can directly count the nodes, otherwise check recursively.
# Time Complexity: O(log(n)^2), Space complexity: O(h^2) => O(log(n))
#
# Solution 2: Binary Search
# https://leetcode.com/problems/count-complete-tree-nodes/discuss/701466/Python-O(log-n-*-log-n)-solution-with-Binary-Search-explained
# Time Complexity: O(log(n)^2), Space complexity: O(h^2) => O(log(n))
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_left_height(self, root: Optional[TreeNode]) -> int:
        height = 0
        current = root
        while current:
            current = current.left
            height += 1
        return height

    def get_right_height(self, root: Optional[TreeNode]) -> int:
        height = 0
        current = root
        while current:
            current = current.right
            height += 1
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)

        if left_height == right_height:
            return 2 ** left_height - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def path(self, root: Optional[TreeNode], num: int) -> bool:
        for s in bin(num)[3:]:
            if s == "0":
                root = root.left
            else:
                root = root.right
            if root is None: return False
        return True

    def countNodes_binarySearch(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left, depth = root, 0

        while left.left:
            left, depth = left.left, depth + 1

        start, end = 2 ** depth, 2 ** (depth + 1) - 1
        if self.path(root, end): return end

        while start + 1 < end:
            middle = (start + end) // 2
            if self.path(root, middle):
                start = middle
            else:
                end = middle
        return start


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)

    r.right = TreeNode(3)
    r.right.left = TreeNode(6)

    print(sol.countNodes_binarySearch(r))  # 6
