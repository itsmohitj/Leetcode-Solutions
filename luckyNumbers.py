"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
"""

# Solution:
# 1. Find the minimum value of each row and store it in min_n
# 2. Find the maximum value of each column and store it in max_n
# 3. Find the intersection of min_n and max_n, store the result in a list and return the list.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_n = {min(rows) for rows in matrix}
        max_n = {max(columns) for columns in zip(*matrix)} 
        return list(min_n & max_n)

# Time Complexity = O(n)
# Space Complexity = O(n)
