# https://leetcode.com/problems/largest-component-size-by-common-factor/
# tags: #array, #math, #union-find
#
# Solution: Union-Find with Prime Factorization
# Explanation at:
# https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/1592263/C%2B%2B-3-Simple-Solution-w-Explanation-or-Disjoint-Set-Union-%2B-Sieve-of-Eratosthenes
# Time complexity: O(n * sqrt(m)), Space complexity O(n*log(m)), m=prime factors
import math
from collections import Counter, defaultdict
from typing import List


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr


class Solution:
    def primes_generator(self, n: int) -> set[int]:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_generator(n // i) | {i}
        return {n}

    def largestComponentSize(self, nums: List[int]) -> int:
        primes = defaultdict(list)
        n = len(nums)
        uf = DSU(n)

        for i, num in enumerate(nums):
            for prime in self.primes_generator(num):
                primes[prime].append(i)

        for prime, indexes in primes.items():
            for i in range(len(indexes) - 1):
                uf.union(indexes[i], indexes[i + 1])

        return max(Counter([uf.find(i) for i in range(n)]).values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestComponentSize(nums=[4, 6, 15, 35]))  # 4
    print(sol.largestComponentSize(nums=[20, 50, 9, 63]))  # 2
    print(sol.largestComponentSize(nums=[2, 3, 6, 7, 4, 12, 21, 39]))  # 8
