# https://leetcode.com/problems/detect-squares/
# tags: #array, #design, #counting, #google, #hash_table
#
# Solution: Two counter dictionaries
# Keep two dictionaries:
# * points_frequency: Count the points, how many times we have each point (duplicates are accepted)
# * x_coords: Count each coordinate x, this is to find all points within this coordinate quickly
# Then, to count we need to find all points with the same coordinate x to reconstruct a square
# Time Complexity: O(1) for add and O(n) for count, Space complexity: O(n)
from collections import Counter, defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points_frequency = Counter()
        self.x_coords = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points_frequency[(x, y)] += 1
        self.x_coords[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for y2 in self.x_coords[x]:
            if y == y2:
                continue
            res += (self.points_frequency[(x, y2)]
                    * self.points_frequency[(x + y2 - y, y)]
                    * self.points_frequency[(x + y2 - y, y2)])
            res += (self.points_frequency[(x, y2)]
                    * self.points_frequency[(x + y - y2, y)]
                    * self.points_frequency[(x + y - y2, y2)])

        return res


if __name__ == '__main__':
    detect_squares = DetectSquares()
    detect_squares.add([3, 10])
    detect_squares.add([11, 2])
    detect_squares.add([3, 2])
    print(detect_squares.count([11, 10]))  # 1
    print(detect_squares.count([14, 8]))  # 0
    detect_squares.add([11, 2])
    print(detect_squares.count([11, 10]))  # 2
