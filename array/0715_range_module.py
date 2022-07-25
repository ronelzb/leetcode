# https://leetcode.com/problems/robot-room-cleaner/
# tags: #design, #google, #ordered_set, #segment_tree
#
# Solution: Binary search
# https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation
# Python slicing: https://stackoverflow.com/questions/509211/understanding-slice-notation
# Time complexity: addRange O(n) - removeRange O(n) - queryRange O(log(n)), space complexity: (n)
# n: number of disjoint intervals currently stored
import bisect


class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        sub_track = []
        if start % 2 == 0:
            sub_track.append(left)
        if end % 2 == 0:
            sub_track.append(right)

        self.track[start: end] = sub_track

    def queryRange(self, left: int, right: int) -> bool:
        left = bisect.bisect_right(self.track, left)
        right = bisect.bisect_left(self.track, right)

        return left == right and left % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        sub_track = []
        if start % 2 == 1:
            sub_track.append(left)
        if end % 2 == 1:
            sub_track.append(right)

        self.track[start: end] = sub_track


if __name__ == '__main__':
    range_module = RangeModule()
    range_module.addRange(10, 20)
    range_module.removeRange(14, 16)
    print(range_module.queryRange(10, 14))  # True
    print(range_module.queryRange(13, 15))  # False
    print(range_module.queryRange(16, 17))  # True
