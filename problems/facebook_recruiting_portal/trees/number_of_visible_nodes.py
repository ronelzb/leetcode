# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=495004218121393&c=896138004629128&ppid=454615229006519&practice_plan=0
# LeetCode similar question:
# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56012/My-simple-accepted-solution(JAVA)
# Time Complexity: O(n), Space complexity: O(n)
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def visible_nodes(self, root: TreeNode, level: int = 0) -> int:
        if root is None: return 0
        left_depth = 1 + self.visible_nodes(root.left, level + 1)
        right_depth = 1 + self.visible_nodes(root.right, level + 1)
        max_depth = max(left_depth, right_depth)
        return max_depth


if __name__ == "__main__":
    sol = Solution()

    root_1 = TreeNode(8)
    root_1.left = TreeNode(3)
    root_1.right = TreeNode(10)
    root_1.left.left = TreeNode(1)
    root_1.left.right = TreeNode(6)
    root_1.left.right.left = TreeNode(4)
    root_1.left.right.right = TreeNode(7)
    root_1.right.right = TreeNode(14)
    root_1.right.right.left = TreeNode(13)

    print(sol.visible_nodes(root_1))  # 4

    root_2 = TreeNode(10)
    root_2.left = TreeNode(8)
    root_2.right = TreeNode(15)
    root_2.left.left = TreeNode(4)
    root_2.left.left.right = TreeNode(5)
    root_2.left.left.right.right = TreeNode(6)
    root_2.right.left = TreeNode(14)
    root_2.right.right = TreeNode(16)

    print(sol.visible_nodes(root_2))  # 5
