# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# tags: #binary_tree, #facebook, #hash_table
#
# Solution 1: Intersection of two linked lists
# The idea for this solution is basically the same as finding the convergence point of 2 intersected linked lists
# We can find the depth difference between the 2 nodes and assign the deeper and shallower nodes
# Then, we up delta levels in the tree to match the levels between the 2 nodes
# After that, we follow their parent pointers until they point to the same node
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 2: Intersection of two linked lists - Optimized
# Instead of calculating the difference between the two nodes initially
# When either of the pointers points to root, we set it to the other original starting node
# Time complexity: O(n), Space complexity: O(1)
from typing import Optional
from utils.tree_traversal_helper import Node


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Optional[Node]:
        def get_depth(x: Node):
            depth = 0
            while x.parent:
                x = x.parent
                depth += 1

            return depth

        p_depth, q_depth = get_depth(p), get_depth(q)
        deeper = p if p_depth >= q_depth else q
        shallower = q if deeper == p else p
        delta_depth = abs(p_depth - q_depth)

        for _ in range(delta_depth):
            deeper = deeper.parent

        while deeper and shallower:
            if deeper == shallower:
                return deeper
            deeper = deeper.parent
            shallower = shallower.parent

        return None

    def lowestCommonAncestor_optimized(self, p: Node, q: Node) -> Optional[Node]:
        p1, q1 = p, q

        while p1 != q1:
            p1 = p1.parent if p1.parent else p
            q1 = q1.parent if q1.parent else q

        return p1


if __name__ == '__main__':
    sol = Solution()

    t = Node(3,
             Node(5,
                  Node(6),
                  Node(2,
                       Node(7),
                       Node(4))),
             Node(1,
                  Node(0),
                  Node(8)))
    print(sol.lowestCommonAncestor_optimized(t.left, t.right))  # 3
    print(sol.lowestCommonAncestor_optimized(t.left.left, t.left.right.right))  # 5
