# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# tags: #array, #string
#
# Solution: Two pass
# The solution here is to do a double iteration and for each ball found, compute the distance and add it to the cost.
# The assumption is when we travel forward we're only considering the balls that are left to the current index,
# similarly when we travel back we're only considering the balls that are to the right of the current index.
# When moving forward, the cost of moving balls to the right for ith index can be computed if we know the total number
# of balls till (i-1)th index and the cost of moving balls till (i-1)th index.
# Time complexity: O(n), Space complexity: O(n)

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        for i in range(n), reversed(range(n)):
            current, steps = 0, 0

            for j in i:
                answer[j] += steps
                current += int(boxes[j])
                steps += current

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(boxes="110"))  # [1,1,3]
    print(sol.minOperations(boxes="001011"))  # [11,8,5,4,3,4]
