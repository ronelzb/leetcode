# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []

        for i, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # dummy node
        head = tail = ListNode(0)

        while heap:
            i, min_value_list = heapq.heappop(heap)[1:]
            tail.next = min_value_list
            tail = tail.next

            if min_value_list.next:
                heapq.heappush(heap, (min_value_list.next.val, i, min_value_list.next))

        return head.next


if __name__ == "__main__":
    input_lists = []

    head_node = ListNode(1)
    head_node.next = ListNode(4)
    head_node.next.next = ListNode(5)
    input_lists.append(head_node)

    head_node = ListNode(1)
    head_node.next = ListNode(3)
    head_node.next.next = ListNode(4)
    input_lists.append(head_node)

    head_node = ListNode(2)
    head_node.next = ListNode(6)
    input_lists.append(head_node)

    sol = Solution()
    head_node = sol.mergeKLists(input_lists)

    current_node = head_node
    while current_node:
        next_node = " -> " if current_node.next else ""
        print(f"{current_node.val}{next_node}", end="")
        current_node = current_node.next
