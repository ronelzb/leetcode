# https://leetcode.com/problems/swap-nodes-in-pairs/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(-1)
        prev.next = head
        head = prev

        while prev and prev.next and prev.next.next:
            current = prev.next
            ahead = current.next
            current.next = ahead.next
            ahead.next = current
            prev.next = ahead
            prev = prev.next.next

        return head.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")

    h = sol.swapPairs(h)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
