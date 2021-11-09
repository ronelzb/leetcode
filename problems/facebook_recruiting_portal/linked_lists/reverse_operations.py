# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=623634548182866&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time complexity: O(n), Space complexity O(1)
from typing import Optional


class Node:
    def __init__(self, x: int):
        self.data = x
        self.next = None

    def __str__(self):
        return str(self.data)


class Solution:
    # noinspection PyUnresolvedReferences
    def reverse(self, head: Optional[Node]) -> Optional[Node]:
        def reverse_nodes(curr: Optional[Node]) -> Optional[Node]:
            prev = None

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        dummy = Node(-1)
        dummy.next = head
        current = head = dummy

        while current.next:
            if current.next.data % 2 != 0:
                current = current.next
            else:
                start = ahead = current.next
                while ahead.next and ahead.next.data % 2 == 0:
                    ahead = ahead.next

                end = ahead.next
                current.next = None
                ahead.next = None

                ahead = reverse_nodes(start)
                current.next = ahead
                while current.next:
                    current = current.next
                current.next = end
        return head.next


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


if __name__ == "__main__":
    sol = Solution()

    head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
    head_1 = sol.reverse(head_1)  # [1, 8, 2, 9, 16, 12]

    c = head_1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")

    head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
    head_2 = sol.reverse(head_2)  # [24, 18, 2, 3, 5, 7, 9, 12, 6]

    c = head_2
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
