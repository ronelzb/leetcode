# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return fast and slow == fast


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(3)
    h.next = ListNode(2)
    h.next.next = ListNode(0)
    h.next.next.next = ListNode(-4)
    h.next.next.next.next = h.next

    assert sol.hasCycle(head=h)

    h = ListNode(1)
    assert not sol.hasCycle(head=h)
