# https://leetcode.com/problems/count-and-say/
class Solution:
    # Solution: Count digits hits until it changes and store it, repeat the process recursively
    # Time complexity: O(n*k) where k is the length of the previous sequence, Space complexity: O(n)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        count = 1
        say = ""

        for i in range(1, len(prev)):
            if prev[i] != prev[i - 1]:
                say += str(count) + str(prev[i - 1])
                count = 0

            count += 1

        say += str(count) + str(prev[-1])
        return say


if __name__ == "__main__":
    sol = Solution()

    print(sol.countAndSay(n=5))
