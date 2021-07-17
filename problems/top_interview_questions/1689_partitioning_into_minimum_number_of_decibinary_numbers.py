# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


if __name__ == "__main__":
    sol = Solution()

    print(sol.minPartitions(n="27346209830709182346"))  # 9
