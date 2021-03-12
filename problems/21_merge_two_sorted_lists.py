class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        last = None

        while l1 or l2:
            if last:
                last.next = ListNode()
                last = last.next
            else:
                last = ListNode()
                l3 = last

            if l1 and (not l2 or l1.val <= l2.val):
                last.val = l1.val
                l1 = l1.next
            else:
                last.val = l2.val
                l2 = l2.next

        return l3


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    sol = Solution()
    l3 = sol.mergeTwoLists(l1, l2)

    while l3:
        print(l3.val)
        l3 = l3.next
