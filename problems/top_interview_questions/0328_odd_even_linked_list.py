# https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        odd = head
        e_head = even = head.next

        while even and even.next:
            odd.next = even.next  # 1 -> 3
            odd = odd.next  # 3
            even.next = odd.next  # 2 -> 4
            even = even.next  # 4

        odd.next = e_head  # 1 -> 3 + 2 -> 4
        return head


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    current = h
    while current:
        print(current, end=" -> ")
        current = current.next
    print("", end="\n")

    h = sol.oddEvenList(h)

    current = h
    while current:
        print(current, end=" -> ")
        current = current.next
    print("", end="\n")
