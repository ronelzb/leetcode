# https://leetcode.com/problems/remove-linked-list-elements/
# tags: #linked_list
#
# Solution: 
# Time complexity: O(n), Space complexity O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        head = current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head.next


if __name__ == "__main__":
    sol = Solution()

    head_1 = ListNode(1)
    head_1.next = ListNode(2)
    head_1.next.next = ListNode(6)
    head_1.next.next.next = ListNode(3)
    head_1.next.next.next.next = ListNode(4)
    head_1.next.next.next.next.next = ListNode(5)
    head_1.next.next.next.next.next.next = ListNode(6)
    head_1 = sol.removeElements(head=head_1, val=6)  # [1,2,6,3,4,5,6]

    c = head_1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
