# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
# tags: #greedy, #string
#
# Solution: Greedy
# We have to generate the string with numeric sum equals to k, and it has n characters
# Input: n = 5, k = 73, Output: "aaszz"
# So, we have n = 5 and our starting character could be a a a a a.
# * First, subtract 5 from k which will comes out 73 - 5 = 68.
# * Then, as you can see 68 is too big, because the maximum we can form is by adding z into it i.e. 25
# So, we will check whether k is minimum against 25, which ever is minimum we'll add into the last character.
# * The result will be subtracted to k itself
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ["a"] * n
        k -= n
        n -= 1

        while k > 0:
            res[n] = chr(1 + min(25, k) + 96)
            k -= min(25, k)
            n -= 1

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSmallestString(n=3, k=27))  # "aay"
    print(sol.getSmallestString(n=3, k=56))  # "dzz"
    print(sol.getSmallestString(n=5, k=73))  # "aaszz"
