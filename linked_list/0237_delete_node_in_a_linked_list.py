# https://leetcode.com/problems/delete-node-in-a-linked-list/
# tags: #linked_list
#
# Solution: Node swap with next node
# Change the value of node with value of next node and then change next element for next of next element
# Time complexity: O(1), Space complexity O(1)
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def deleteNode(self, node: Optional[ListNode]) -> None:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(4)
    h.next = ListNode(5)
    h.next.next = ListNode(1)
    h.next.next.next = ListNode(9)
    sol.deleteNode(h.next)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")


