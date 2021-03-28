class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [True if i > 1 else False for i in range(n)]

        for i in range(2, n):
            if primes[i]:
                count += 1
                j = 2

                while i * j < n:
                    primes[i * j] = False
                    j += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.countPrimes(10) == 4
    # assert sol.countPrimes(0) == 0
    # assert sol.countPrimes(1) == 0
