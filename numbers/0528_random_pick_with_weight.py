# https://leetcode.com/problems/random-pick-with-weight/
# tags: #binary_search, #google, #math, #prefix_sum, #randomized
#
# Solution: Alias method
# https://en.wikipedia.org/wiki/Alias_method
# Time complexity: init=O(n) pickIndex=O(1), Space complexity: O(n)
from collections import namedtuple
import random
from typing import List
Box = namedtuple('Box', ('small', 'big', 'div'))


class Solution:

    def __init__(self, w: List[int]):
        self.n, self.size = len(w), sum(w)
        self.boxes = []

        w = [x * self.n for x in w]
        bigs = {i: x for i, x in enumerate(w) if x >= self.size}
        smalls = {i: x for i, x in enumerate(w) if x < self.size}

        while smalls:
            big = next(iter(bigs))
            small, div = smalls.popitem()
            self.boxes.append(Box(small, big, div))
            bigs[big] -= self.size - div

            if bigs[big] < self.size:
                smalls[big] = bigs.pop(big)

        self.boxes += [Box(0, big, 0) for big in bigs]

    def pickIndex(self) -> int:
        box = random.choice(self.boxes)
        weight = random.randint(0, self.size)
        return box.big if weight >= box.div else box.small
