# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# tags: #array, #design, #facebook, #hash_table, #two_pointers
#
# Solution 1: Dictionaries intersection
# Store the non-zero values and their corresponding indices in a dictionary, with the index being the key.
# When calculating the dotProduct find the intersection between the 2 dictionaries.
# This solution has a fundamental problem: Hashing large sparse vectors
# when two keys are the same as will frequently be the case here, they will hash to the same bucket,
# which means the hash map will store them in a linked list (or possibly a tree).
# As you get more and more keys your hash map will devolve into linear, rather than constant time performance.
# If you have a billion items in your vector this will impact in performance dramatically
# Time complexity: O(n), Space complexity O(n) for init; O(1) for dotProduct
#
# Solution 2: Two pointers
# We can also represent elements of a sparse vector as a list of index, value pairs.
# We use two pointers to iterate through the two vectors to calculate the dot product
# Time complexity: O(n) for init; O(L+L2) for dotProduct, Space complexity O(L) for init, O(1) for dotProduct
from typing import List


class SparseVectorDict:
    def __init__(self, nums: List[int]):
        self.non_zero_vals = {i: v for i, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVectorDict') -> int:
        res = 0

        for index, val in vec.non_zero_vals.items():
            if index in self.non_zero_vals:
                res += val * self.non_zero_vals[index]

        return res


class SparseVectorPointers:
    def __init__(self, nums: List[int]):
        self.pairs = [(i, v) for i, v in enumerate(nums) if v != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVectorPointers') -> int:
        res = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                res += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return res


if __name__ == '__main__':
    v1 = SparseVectorPointers([1, 0, 0, 2, 3])
    v2 = SparseVectorPointers([0, 3, 0, 4, 0])
    print(v1.dotProduct(v2))  # 8
