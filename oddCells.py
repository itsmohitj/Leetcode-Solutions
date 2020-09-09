"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
"""

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for ri,ci in indices:
            rows[ri] += 1
            cols[ci] += 1

        res=0
        for i in range(n):
            for j in range(m):
                if (rows[i]+cols[j]) % 2 == 1:
                    res +=1
        return res

# Time Complexity = O(m*n)
# Space Complexity = O(m+n)
