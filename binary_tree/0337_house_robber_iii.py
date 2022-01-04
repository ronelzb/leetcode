# https://leetcode.com/problems/house-robber-iii/
# tags: #dfs, #dp
#
# Solution: DFS + Dynamic programming
# We can make a single dfs call to left and right child nodes (without differentiating the state of current node) and
# return the results for both the cases of the child nodes being robbed and not robbed:
# * When current node is robbed which will be equal to current node's value + sum of result of child nodes
# not being robbed.
# * When current node is NOT robbed which will be equal to sum of result of child nodes in their maximum loot state.
# This approach issues a single dfs call down till the leaf node and from there it propagates upwards with a tuple:
# * The first value is the maximum loot when current node is not robbed and,
# * The second value is when the maximum loot when current node is robbed
# Time complexity: O(n), Space complexity O(h) => O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple:
            if not root: return 0, 0
            left, right = dfs(root.left), dfs(root.right)
            return max(left) + max(right), root.val + left[0] + right[0]

        return max(dfs(root))


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(3)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.right = TreeNode(3)
    r.right.right = TreeNode(1)
    print(sol.rob(r))  # 7

    r = TreeNode(4)
    r.left = TreeNode(1)
    r.left.left = TreeNode(2)
    r.left.left.left = TreeNode(3)
    print(sol.rob(r))  # 7
