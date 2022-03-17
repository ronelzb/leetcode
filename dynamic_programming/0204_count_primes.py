# https://leetcode.com/problems/count-primes/
# tags: #array, #dp, #enumeration, #math, #must_do_easy_questions, #number_theory, #top_interview_questions
#
# Solution: Dynamic Programming - Sieve of Eratosthenes optimized
# https://leetcode.com/problems/count-primes/discuss/1200796/JS-Python-Java-C%2B%2B-or-Easy-Sieve-of-Eratosthenes-Solution-w-Explanation
# Time complexity: O(n*log(log(n))), Space complexity: O(n)
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
    print(sol.countPrimes(10))  # 4
    print(sol.countPrimes(0))  # 0
    print(sol.countPrimes(1))  # 0
