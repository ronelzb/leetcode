# https://leetcode.com/problems/path-sum-iii/
# tags: #binary_tree, #dfs
#
# Explanation at:
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
#
# Solution 1: DFS + Prefix sum
# The idea is based on path.
# The dict stores <prefix sum, frequency> pairs before getting to the current node. We can imagine a path from the root
# to the current node. The sum from any node in the middle of the path to the current node = the difference between the
# sum from the root to the current node and the prefix sum of the node in the middle.
# We are looking for some consecutive nodes that sum up to the given target value, which means the difference found
# in the dictionary should be equal to the target value. In addition, we need to know how many differences are equal to
# the target value.
#
# "Why do you minus one in the last line of code?"
# If left subtree has been scanned, preSum has to remove this path, because this path is not the prefix path of
# the right subtree. Same as the left subtree, when right subtree is scanned, the path should be removed too.
# Time Complexity: O(n), Space complexity: O(n)
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def prefixSum(node: Optional[TreeNode], current_sum: int) -> int:
            if node is None: return 0

            current_sum += node.val
            result = prefixes[current_sum - targetSum]
            prefixes[current_sum] += 1

            result += prefixSum(node.left, current_sum) + prefixSum(node.right, current_sum)
            prefixes[current_sum] -= 1
            return result

        prefixes = defaultdict(int)
        prefixes[0] = 1
        return prefixSum(root, 0)


if __name__ == "__main__":
    sol = Solution()

    r = TreeNode(10)
    r.left = TreeNode(5)
    r.left.left = TreeNode(3)
    r.left.left.left = TreeNode(3)
    r.left.left.right = TreeNode(-2)
    r.left.right = TreeNode(2)
    r.left.right.right = TreeNode(1)

    r.right = TreeNode(-3)
    r.right.right = TreeNode(11)

    print(sol.pathSum(r, 8))  # 3
