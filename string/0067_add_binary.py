# https://leetcode.com/problems/add-binary/
# tags: #string
#
# Solution 1: Bit by bit computation
# Time Complexity: O(max(m, n)), Space complexity: O(max(m, n))
#
# Solution 2: Using built-in functions
# Time Complexity: O(max(m, n)), Space complexity: O(max(m, n))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, m, n = 0, len(a), len(b)
        i, j = m - 1, n - 1
        result = []
        while i >= 0 or j >= 0:
            bin_sum = carry
            if i >= 0:
                bin_sum += int(a[i])
                i -= 1
            if j >= 0:
                bin_sum += int(b[j])
                j -= 1
            result.insert(0, bin_sum % 2)
            carry = bin_sum // 2

        if carry > 0: result.insert(0, 1)

        return "".join([str(x) for x in result])

    def addBinary_builtin(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary_builtin(a="11", b="1"))  # "100"
    print(sol.addBinary_builtin(a="1010", b="1011"))  # "10101"
    print(sol.addBinary_builtin(a="1", b="111"))  # ""1000""
