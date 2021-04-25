# Rearrange a singly linked list 1 -> 2 -> 3 -> ... -> n-1 -> n,
# So that it will result 1 -> n-2 -> 2 -> n-1 -> 3 -> n
# Reverse a linked list: https://www.geeksforgeeks.org/reverse-a-linked-list/
# Rearrange linked list: https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head: ListNode) -> ListNode:
    prev = next_node = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def rearrange_list(head: ListNode) -> None:
    slow = fast = head

    # find list half using tortoise and hare algorithm
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # split the list into two halves
    head2 = slow.next
    slow.next = None

    # reverse last half
    head2 = reverse(head2)

    # rearrange: merge those two lists into a new one in-place
    current = temp = ListNode(-1)
    while head or head2:
        if head:
            current.next = head
            current = current.next
            head = head.next

        if head2:
            current.next = head2
            current = current.next
            head2 = head2.next

    head = temp.next
    print_list(head)


def print_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next


if __name__ == "__main__":
    ll = ListNode(1)
    current_node = ll

    for i in range(2, 7):
        next_value = ListNode(i)
        current_node.next = next_value
        current_node = current_node.next

    rearrange_list(ll)
