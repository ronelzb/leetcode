# https://leetcode.com/problems/reverse-linked-list-ii/
# tags: #linked_list
#
# Solution: One pass + reverse
# Find pre_start (left - 1) and end (right) nodes, from there reverse the nodes and reallocate pointers
# Time complexity: O(n), Space complexity O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_nodes(current: Optional[ListNode]) -> Optional[ListNode]:
            prev = None

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        if left == right: return head

        dummy = ListNode(-1)
        dummy.next = head
        head = behind = ahead = dummy
        for i in range(right):
            if i < left - 1: behind = behind.next
            ahead = ahead.next

        behind_next = behind.next
        ahead_next = ahead.next
        ahead.next = None
        behind.next = reverse_nodes(behind_next)
        while behind.next:
            behind = behind.next
        behind.next = ahead_next

        return head.next


if __name__ == "__main__":
    sol = Solution()

    head_1 = ListNode(1)
    head_1.next = ListNode(2)
    head_1.next.next = ListNode(3)
    head_1.next.next.next = ListNode(4)
    head_1.next.next.next.next = ListNode(5)
    head_1 = sol.reverseBetween(head_1, 2, 4)  # [1,4,3,2,5]

    c = head_1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
