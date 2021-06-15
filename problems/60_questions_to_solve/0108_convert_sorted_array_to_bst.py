# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        n = len(nums)
        half = n // 2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[0:half])
        root.right = self.sortedArrayToBST(nums[half + 1:n])

        return root


def traverse_preorder(node: TreeNode, level: int = 0) -> str:
    output = " " * level + str(node)

    if node.left:
        output += "\n" + traverse_preorder(node.left, level + 1)
    if node.right:
        output += "\n" + traverse_preorder(node.right, level + 1)

    return output


if __name__ == "__main__":
    sol = Solution()

    t = sol.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    print(traverse_preorder(t))
