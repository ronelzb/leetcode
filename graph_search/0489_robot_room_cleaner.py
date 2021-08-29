# https://leetcode.com/problems/robot-room-cleaner/
# tags: #backtracking, #dfs, #google, #graph_search
#
# The idea here is to cover all the area where the robot can get into (ones in the matrix)
# starting from the given location
# We can use dfs here with the tweak of moving the robot back to the original position
# As recursive traversal suggests
#
# Time complexity: O(m * n), space complexity: (m * n)
"""
    # This is the robot's control interface.
    # You should not implement it, or speculate about its implementation
    class Robot:
        # Returns true if the cell in front is open and robot moves into the cell.
        # Returns false if the cell in front is blocked and robot stays in the current cell.
        def move() -> bool:

        # Robot will stay in the same cell after calling turnLeft/turnRight.
        # Each turn will be 90 degrees.
        def turnLeft() -> None:
        def turnRight() -> None:

        # Clean the current cell.
        def clean() -> None:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3
"""
class Solution:
    def cleanRoom(self, robot) -> None:
        coordinates_cleansed = set(tuple)
        robot.clean()

        # direction is clockwise starting up: 0=up, 1=right, 2=down, 3=left
        def dfs(i, j, direction):
            if (i, j) in coordinates_cleansed:
                return
            coordinates_cleansed.add((i, j))

            for i in range(4):
                if robot.move():
                    x, y = i, j
                    if direction == 0:
                        x += 1
                    elif direction == 1:
                        y += 1
                    elif direction == 2:
                        y -= 1
                    elif direction == 3:
                        x -= 1
                    dfs(x, y, direction)

                    # turn back robot to the original position
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()

                    # redirect robot to previous direction
                    robot.turnRight()
                    robot.turnRight()

                robot.turnRight()
                direction = (direction + 1) % 4

        dfs(0, 0, 0)
