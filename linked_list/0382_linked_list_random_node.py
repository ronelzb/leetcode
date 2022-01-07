# https://leetcode.com/problems/linked-list-random-node/
# tags: #math, #randomized, #reservoir_sampling
#
# Solution: Reservoir Sampling
# Explanation:
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
# https://www.geeksforgeeks.org/reservoir-sampling/
# Explanation video: https://www.youtube.com/watch?v=A1iwzSew5QY&t=1s
# Time complexity: O(n), Space complexity O(1)
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current, next_node, index = self.head, self.head.next, 1

        while next_node:
            if random.randint(0, index) == 0:
                current = next_node
            next_node = next_node.next
            index += 1
        return current.val


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    sol = Solution(l1)
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
