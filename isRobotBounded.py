"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_move, start, dir = ([-1, 0], [0, -1], [1, 0], [0, 1]), [0,0], 0
        for i in range(4):
            for x in instructions:
                if x == "G":
                    start[0] += dir_move[dir][0]
                    start[1] += dir_move[dir][1]
                if x == "L":
                    dir = (dir + 1) % 4
                if x == "R":
                    dir = (dir - 1) % 4
        return True if start == [0,0] else False

# Time Complexity = O(n) where n is the length of the instructions
# Space Complexity = O(1)
