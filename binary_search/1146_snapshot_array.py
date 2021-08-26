# https://leetcode.com/problems/snapshot-array/
# tags: #binary_search, #data_structures, #google
# Idea: save only new values with the current snap_id at the specified index
# We binary search on arr index to find the version, which has largest snapId <= snapId
# Time complexity: constructor=O(n), get=O(log n), Space complexity: O(n)
class SnapshotArray:
    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        snap_sub_array = self.snapshots[index]
        if len(snap_sub_array) == 0 or snap_sub_array[-1][0] < self.snap_id:
            snap_sub_array.append([self.snap_id, 0])
        snap_sub_array[-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_sub_array = self.snapshots[index]

        left = 0
        right = len(snap_sub_array) - 1
        ans = -1

        while left <= right:
            middle = (left + right) // 2

            if snap_sub_array[middle][0] <= snap_id:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1

        return snap_sub_array[ans][1] if ans > -1 else 0


if __name__ == "__main__":
    snap = SnapshotArray(1)
    snap.snap()
    snap.snap()
    snap.set(0, 4)

    snap.snap()
    print("snap", snap.get(0, 1))  # 4
    snap.set(0, 12)
    print("snap", snap.get(0, 1))  # 4

    snap.snap()
    print("snap", snap.get(0, 3))  # 1
