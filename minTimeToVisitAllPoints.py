"""On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
"""

"""
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
"""

"""
Solution:
    Consider two points pt1 = (x1,y1) and pt2 = (x2,y2). We can move diagonally until either x1 equals x2 or y1 equals y2(whichever happens first).
    After that, We only have to move in horizontal or vertical direction i.e.if x1 = x2 then we have to cover the distance from y1 to y2 in vertical direction.
    So, a diagonal move is the same as a up or down move the amount of time is just the max of the x or y distance. 
    For example say we are at 0,0 and want to get to 2,3. We would move 2 in the X and 3 in the Y. But becuase we could get to 2,2 in two moves we only need the one additional up.
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        n = len(points)
        for i in range(n - 1):
            pt1 = points[i]
            pt2 = points[i+1]
            time += max(abs(pt2[1]-pt1[1]),abs(pt2[0]-pt1[0]))
        return time

# Time Complexity = O(n)
# Space Complexity = O(1)
