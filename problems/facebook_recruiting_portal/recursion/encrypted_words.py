# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=223547538732703&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n), Space complexity: O(n)
class Solution:
    def findEncryptedWord(self, s: str) -> str:
        n = len(s)
        if n <= 2: return s

        middle = n // 2 - (1 if n % 2 == 0 else 0)
        return s[middle] + self.findEncryptedWord(s[0: middle]) + self.findEncryptedWord(s[middle + 1: n])


if __name__ == "__main__":
    sol = Solution()
    print(sol.findEncryptedWord(s="abcxcba"))  # "xbacbca"
    print(sol.findEncryptedWord(s="facebook"))  # "eafcobok"
