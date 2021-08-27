# https://leetcode.com/problems/zigzag-conversion/
# tags: #array, #string
#
# Naive solution: Convert input into zigzagged matrix and traversed it
#
# Optimal solution Traverse input in a zigzag way
# https://leetcode.com/problems/zigzag-conversion/discuss/3435/If-you-are-confused-with-zigzag-patterncome-and-see!
# https://leetcode.com/problems/zigzag-conversion/discuss/545622/Python-100-easy-understand-solution
# Given n = numRows, we see that each cycle consists of (2 * rows - 2) elements
#
# Optimal Time complexity: O(n), Space complexity: O(1)
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        n, i = len(s), 0
        matrix = []
        output = ""

        while i < n:
            matrix.append([None] * num_rows)
            iterations_to = min(i + num_rows, n)
            row = 0
            while i < iterations_to:
                matrix[-1][row] = s[i]
                row += 1
                i += 1

            row = num_rows - 2
            while row > 0 and i < n:
                matrix.append([None] * num_rows)
                matrix[-1][row] = s[i]
                row -= 1
                i += 1

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] is not None:
                    output += matrix[i][j]

        return output

    def convert_optimal(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        output = ""
        step = 2 * num_rows - 2

        for i in range(num_rows):
            for j in range(0, n - i, step):
                output += s[i + j]
                if 0 < i < num_rows - 1 and j + step - i < n:
                    output += s[j + step - i]

        return output


if __name__ == "__main__":
    sol = Solution()
    assert sol.convert_optimal(s="PAYPALISHIRING", num_rows=3) == "PAHNAPLSIIGYIR"
    assert sol.convert_optimal(s="PAYPALISHIRING", num_rows=4) == "PINALSIGYAHRPI"
