# https://leetcode.com/problems/path-sum/
# tags: #binary_tree, #dfs
#
# Most of the solutions you will find uses subtraction on the current node's value.
# Instead, I used a different approach: To sum the path in preorder fashion until we reach
# the tree leaves and there we check if the targetSum == pathSum
#
# Time complexity: O(n), Space complexity: O(n) stack trace recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int, pathSum: int = 0) -> bool:
        if root is None:
            return False

        pathSum += root.val
        
        if root.left is None and root.right is None:  # leaf
            return targetSum == pathSum

        return self.hasPathSum(root.left, targetSum, pathSum) or self.hasPathSum(root.right, targetSum, pathSum)


if __name__ == "__main__":
    sol = Solution()

    t = TreeNode(5)

    t.left = TreeNode(4)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)

    t.right = TreeNode(8)
    t.right.left = TreeNode(13)
    t.right.right = TreeNode(4)
    t.right.right.right = TreeNode(1)

    print(sol.hasPathSum(t, 22))  # True
