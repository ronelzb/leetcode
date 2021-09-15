# https://leetcode.com/problems/merge-k-sorted-lists/
# tags: #heap, #linked_list, #merge_sort
#
# Interesting discussions about time/space complexities:
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10528/A-java-solution-based-on-Priority-Queue
#
# Solution 1: Heap
# Time complexity: O(n*log(k)) n=total elements / k=len(lists), Space complexity: O()
#
# Solution 2: Merge sort
# Use Merge sort to join list nodes in pairs, if the current lists size is odd then
# append unvisited list in current iteration
# Time complexity: O(n*log(k)), Space complexity: O(k)
import heapq
from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists_heap(self, lists: List[ListNode]) -> ListNode:
        heap = []

        for i, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        head = tail = ListNode(0)
        while heap:
            i, min_value_list = heapq.heappop(heap)[1:]
            tail.next = min_value_list
            tail = tail.next

            if min_value_list.next:
                heapq.heappush(heap, (min_value_list.next.val, i, min_value_list.next))

        return head.next

    def mergeKLists_mergeSort(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None

        def merge(a: ListNode, b: ListNode) -> ListNode:
            tail = head = ListNode(0)

            while a is not None and b is not None:
                if a.val < b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next

            if a is not None:
                tail.next = a
            else:
                tail.next = b

            return head.next

        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists) - 1, 2):
                new_lists.append(merge(lists[i], lists[i + 1]))

            if len(lists) % 2 == 1:
                new_lists.append(lists[len(lists) - 1])
            lists = new_lists

        return lists[0]


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
    head_node = sol.mergeKLists_mergeSort(input_lists)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

    current_node = head_node
    while current_node:
        next_node = " -> " if current_node.next else ""
        print(f"{current_node.val}{next_node}", end="")
        current_node = current_node.next
