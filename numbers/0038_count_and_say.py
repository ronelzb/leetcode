# https://leetcode.com/problems/count-and-say/
# tags: #string, #top_interview_questions
#
# Solution: Recursion + counter
# Count digits hits until it changes and store it, repeat the process recursively
# Time complexity: O(n*k) where k is the length of the previous sequence, Space complexity: O(n)
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        prev = self.countAndSay(n - 1)
        count = 1
        say = ""

        for i in range(1, len(prev) + 1):
            if i == len(prev) or prev[i] != prev[i - 1]:
                say += str(count) + str(prev[i - 1])
                count = 0
            count += 1

        return say


if __name__ == "__main__":
    sol = Solution()

    print(sol.countAndSay(n=4))  # "1211"
    print(sol.countAndSay(n=5))  # "111221"
