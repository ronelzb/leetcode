# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        prev = ListNode(-1)
        prev.next = head
        head = prev

        while current and current.next:
            if current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return head.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    h.next = ListNode(1)
    h.next.next = ListNode(2)
    h.next.next.next = ListNode(2)
    h.next.next.next.next = ListNode(3)
    h.next.next.next.next.next = ListNode(3)
    h.next.next.next.next.next.next = ListNode(4)
    h.next.next.next.next.next.next.next = ListNode(5)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next

    h = sol.deleteDuplicates(h)  # [1, 4, 5]
    print("", end="\n")
    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
