# https://leetcode.com/problems/rotate-list/
# tags: #linked_list, #two_pointers
#
# Solution: Two pointers
# Since n may be a large number compared to the length of list, we need to know the length of linked list.
# After that, move the list after the (n-k%n )th node to the front to finish the rotation.
# Time Complexity: O(n), Space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        k = k % n if k >= n else k
        if k == 0:
            return head

        # Get total length
        i = 0
        slow = fast = head
        while i < k and fast:
            fast = fast.next
            i += 1

        # Find breaking point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Do the rotation
        slow.next, slow = None, slow.next
        fast = slow
        while fast and fast.next:
            fast = fast.next

        fast.next = head
        head = slow

        return head


def print_list(h: ListNode):
    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")


if __name__ == "__main__":
    sol = Solution()

    # h = ListNode(1)
    # h.next = ListNode(2)
    # h.next.next = ListNode(3)
    # h.next.next.next = ListNode(4)
    # h.next.next.next.next = ListNode(5)
    # h = sol.rotateRight(h, 2)  # [4,5,1,2,3]
    # print_list(h)

    # h = ListNode(0)
    # h.next = ListNode(1)
    # h.next.next = ListNode(2)
    # h = sol.rotateRight(h, 4)
    # print_list(h)  # [2, 0, 1]

    h = ListNode(1)
    h.next = ListNode(2)
    h = sol.rotateRight(h, 2)
    print_list(h)  # [2, 0, 1]
