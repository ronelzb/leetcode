# https://leetcode.com/problems/reverse-nodes-in-k-group/
# tags: #tag1
#
# Solution: Reverse Linked List and two pointers
# Credits to this explanation:
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/183356/Java-O(n)-solution-with-super-detailed-explanation-and-illustration
# Time Complexity: O(n), Space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse_nodes(start: ListNode, end: ListNode) -> ListNode:
            prev = None
            curr = start.next

            while curr != end:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            tail = start.next
            tail.next = curr
            start.next = prev
            return tail

        dummy = current = ListNode(0)
        dummy.next = head
        while current:
            ahead = current

            i = 0
            while i < k and ahead is not None:
                ahead = ahead.next
                i += 1
            if ahead is None:
                break

            current = reverse_nodes(current, ahead.next)

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    c = h
    for l in range(2, 6):
        c.next = ListNode(l)
        c = c.next

    h = sol.reverseKGroup(h, 2)

    print("", end="\n")
    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
