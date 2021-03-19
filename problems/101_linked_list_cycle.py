class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        if not head:
            return False

        current = head
        runner = head.next

        while runner and runner.next:
            if current == runner:
                return True

            current = current.next
            runner = runner.next.next

        return False


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert sol.has_cycle(head)
