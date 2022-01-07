# https://leetcode.com/problems/insert-delete-getrandom-o1/
# tags: #array, #hash_table, #math, #randomized
#
# Solution: Dictionary + randomize
# We can think of using set + list, and we will get the desired time complexity when getting the random
# BUT it's impossible to remove an item in O(1) in this manner, to solve this issue we use a dictionary instead.
# Where the dictionary will store as value the current val's index in the list and when performing the removal
# swap last item index with removed val
# Time complexity: average O(1), Space complexity: O(2 * n) => O(n)
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_items = dict()
        self.items = []
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map_items:
            self.map_items[val] = self.length
            self.items.append(val)
            self.length += 1
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map_items:
            return False

        # Move last item to val's index in the dictionary and list to keep consistency
        last_element_in_list = self.items[-1]
        element_to_remove_index = self.map_items[val]

        self.map_items[last_element_in_list] = element_to_remove_index
        self.items[element_to_remove_index] = last_element_in_list

        del self.map_items[val]
        self.items.pop()
        self.length -= 1

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.items)


if __name__ == "__main__":
    r = RandomizedSet()
