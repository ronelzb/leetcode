# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# tags: #linked_list, #two_pointers
#
# Solution: One pass
# Move fast pointer to the n - 1 places forward, then move both at the same speed.
# Eventually, when the fast pointer reaches the end, the slow pointer will be n-1 places behind
# From there just verify the edge case if n == len(list) to move the head to the next pointer
# For the rest of the cases set slow pointer.next to the subsequent element
#
# Time complexity: O(n), Space complexity: O(1)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        ahead = head
        while i < n and ahead:
            ahead = ahead.next
            i += 1

        if i < n:
            return head

        current = head
        while ahead and ahead.next:
            ahead = ahead.next
            current = current.next

        if current == head and ahead is None:
            head = head.next
        else:
            current.next = current.next.next

        return head


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(2)
    head_node.next.next = ListNode(3)
    head_node.next.next.next = ListNode(4)
    head_node.next.next.next.next = ListNode(5)

    sol = Solution()
    head_node = sol.removeNthFromEnd(head_node, 5)

    current_node = head_node
    while current_node:
        next_node = " -> " if current_node.next else ""
        print(f"{current_node.val}{next_node}", end="")
        current_node = current_node.next
