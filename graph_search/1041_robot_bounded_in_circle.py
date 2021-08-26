# https://leetcode.com/problems/robot-bounded-in-circle/
# tags: #amazon, #one_pass, #graph_search
#
# Solution: The problem says at then end "Return true if and only if there exists a circle in the plane such that
# the robot never leaves the circle."
# AND hint #2 says: The robot stays in the circle iff (looking at the final vector)
# it changes direction (ie. doesn't stay pointing north), or it moves 0.
#
# With above premises we can infer there is 2 outcomes when the result is true:
# 1. When the robot finishes in position (0,0) no matter where is facing to or
# 2. When final direction is different than towards
#
# Time complexity: 0(n), Space complexity: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        pos = [0, 0]

        for c in instructions:
            if c == "G":
                pos[0] += direction[0]
                pos[1] += direction[1]
            elif c == "L":
                direction = (-direction[1], direction[0])
            else:  # c == "R"
                direction = (direction[1], -direction[0])

        return pos == [0, 0] or direction != (0, 1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.isRobotBounded(instructions="GGLLGG"))  # True
    print(sol.isRobotBounded(instructions="GLRLLGLL"))  # False
