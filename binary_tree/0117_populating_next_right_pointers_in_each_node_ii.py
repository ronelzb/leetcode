# https://leetcode.com/problems/binary-tree-level-order-traversal/
# tags: #bfs, #dfs, #linked_list
#
# Solution: Breadth-first search
# Use BFS to traverse the tree, at each level of the given tree use a list to keep the last seen node
# When a new node to the right is visited then point the prev.next = new. Another approach is to traverse
# the tree horizontally by level
# Time complexity: O(n), Space complexity: O(h)
#
# Solution Follow up: Recursion + BFS
# This solution will track the head at each level and use that not null head to define the next iteration
# Time complexity: O(n), Space complexity: O(1)
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None

        queue = deque([(root, 0)])
        last_node_by_level = []

        while queue:
            node, lvl = queue.popleft()
            if len(last_node_by_level) < lvl + 1:
                last_node_by_level.append(node)
            else:
                last_node_by_level[lvl].next = node
                last_node_by_level[lvl] = node

            if node.left: queue.append((node.left, lvl + 1))
            if node.right: queue.append((node.right, lvl + 1))

        return root

    def connect_follow_up(self, root: 'Node') -> 'Node':
        if root is None: return None

        dummy = Node(-1)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal

            # iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next

            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node

        return root


if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.left.left = Node(4)
    t.left.right = Node(5)

    t.right = Node(3)
    t.right.right = Node(7)

    s = Solution()
    t = s.connect_follow_up(t)
