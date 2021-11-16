# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# tags: #binary_search
#
# Solution: Binary Search
# Since m*n is 900 million, we need something faster than linear.
# Say count is true if and only if there are k or more values in the multiplication table
# that are less than or equal to x.
#
# Let's count how many values in the multiplication table are less than or equal to x.
# In the i-th row, the table looks like [i, 2*i, 3*i, ..., n*i].
# The largest possible k*i that could appear is x // i.
# However, if x is really big, then perhaps k > n, so we need to actually take min(x // i, n).
#
# We should take the sum of these over all such i.
# After we have the count, we want to know if that count is greater than or equal to k
#
# Another explanation at:
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/262279/Python-Binary-Search-Need-to-Return-the-Smallest-Candidate
#
# Time complexity: O(min(n,m)*log(m*n)), Space complexity O(1)
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        while left < right:
            middle, count = (left + right) // 2, 0
            j = n
            for i in range(1, m + 1):
                while j >= 1 and i * j > middle:
                    j -= 1
                count += j

            if count >= k:
                right = middle
            else:
                left = middle + 1

        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthNumber(m=3, n=3, k=5))  # 3
