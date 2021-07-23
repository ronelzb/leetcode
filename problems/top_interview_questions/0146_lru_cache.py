# https://leetcode.com/problems/lru-cache/
import collections


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # Solution: Doubly linked list to store (key, val) pair + dictionary mapping the key to the corresponding node
    # To avoid extra complexity in the code, initialized head and tail with a dummy node and
    # doubly linked list will be reversed, tail will be the most recently used
    # Time complexity: O(1), Space complexity: O(capacity)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.key2node = dict()
        self.tail = self.head = ListNode(-1, -1)

    # When get a key move it to head as it was recently used
    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        if node.next:  # if it has a more recently used then move it to front (tail)
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            if node.next:  # if it has a more recently used then move it to front (tail)
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
            node.val = value
        else:
            new_node = ListNode(key, value)
            self.key2node[key] = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

            if self.length > self.capacity:
                node2remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.key2node[node2remove.key]
                self.length -= 1


class LRUCacheSortedDict:
    # Workaround solution: Use built-in sortedDict, if this is used in the interview
    # The interviewer will probably ask about sortedDict basic implementation depending on the time left
    def __init__(self, capacity):
        self.capacity = capacity
        self.sorted_dict = collections.OrderedDict()

    def get(self, key):
        if key not in self.sorted_dict:
            return -1
        self.sorted_dict.move_to_end(key, last=False)
        return self.sorted_dict[key]

    def put(self, key, val):
        self.sorted_dict[key] = val
        self.sorted_dict.move_to_end(key, last=False)

        if len(self.sorted_dict) > self.capacity:
            self.sorted_dict.popitem()


if __name__ == "__main__":
    lruCache = LRUCacheSortedDict(2)
    lruCache.put(1, 1)
    lruCache.put(2, 2)
    print(lruCache.get(1))  # 1
    lruCache.put(3, 3)
    print(lruCache.get(2))  # -1
    lruCache.put(4, 4)
    print(lruCache.get(3))  # 3
    print(lruCache.get(1))  # -1
