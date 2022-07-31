# https://leetcode.com/problems/range-sum-query-mutable/
# tags: #array, #design, #binary_indexed_tree, #segment_tree
#
# Solution: Binary Indexed Tree
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
# Time complexity: init=O(n*log(n)) update/sumRange=O(log(n)), Space complexity: O(n)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.bit[k] += nums[i]
                k += (k & -k)

    def update(self, index: int, val: int) -> None:
        diff, self.nums[index] = val - self.nums[index], val
        index += 1
        while index <= self.n:
            self.bit[index] += diff
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        res, right = 0, right + 1

        while right:
            res += self.bit[right]
            right -= (right & -right)
        while left:
            res -= self.bit[left]
            left -= (left & -left)

        return res


if __name__ == '__main__':
    num_array = NumArray([1, 3, 5])
    print(num_array.sumRange(0, 2))  # 9
    num_array.update(1, 2)
    print(num_array.sumRange(0, 2))  # 8
