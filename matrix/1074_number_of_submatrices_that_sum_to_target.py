# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# tags: #array, #google, #hash_table, #matrix
#
# Great solution explanation at:
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum
# Complex problem from simpler: https://leetcode.com/problems/subarray-sum-equals-k/
#
# This problem can be decomposed as follows:
# 1. Calculate prefix sum for each row
# 2. For every possible range between two columns, aggregate the prefix sum of sub-matrices that can be formed
# between those two columns by adding the sum of values between them for each row (sub array sum equals k)
#
# Time complexity: O(m*n + m*n^2) => O(m*n^2), Space complexity: O(m) sums dict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        for row in matrix:
            for i in range(1, n):
                row[i] += row[i - 1]

        count = 0
        for i in range(n):
            for j in range(i, n):
                sums = dict()
                current_sum, sums[0] = 0, 1

                for k in range(m):
                    current_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += sums.get(current_sum - target, 0)
                    sums[current_sum] = sums.get(current_sum, 0) + 1

        return count


if __name__ == "__main__":
    sol = Solution()

    print(sol.numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))  # 4
