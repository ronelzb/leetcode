# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = next_node = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def reorderList(self, head: ListNode) -> None:
        # This problem can be split in 3 steps:
        # 1. Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. From middle revert linked list
        second_half = slow.next
        slow.next = None
        second_half = self.reverse(second_half)

        # 3. Merge first mid and second reversed mid
        first_half = head
        head = ListNode(-1)  # helper node
        while first_half or second_half:
            if first_half:
                head.next = first_half
                first_half = first_half.next
                head = head.next

            if second_half:
                head.next = second_half
                second_half = second_half.next
                head = head.next

        head = head.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    curr = h
    for i in range(2, 6):
        curr.next = ListNode(i)
        curr = curr.next

    sol.reorderList(head=h)
    curr = h
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
