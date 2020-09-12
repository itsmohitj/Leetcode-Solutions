"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Input: [1,2,3,3]
Output: 3

"""

# Solution 1:

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return (sum(A) - sum(set(A))) // (len(A) - len(set(A)))

# Time Complexity = O(n)
# Space Complexity = O(1)

# Solution 2:

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hash = []
        for i in A:
            if i in hash:
                return i
            hash.append(i)

# Time Complexity = O(n^2)
# Space Complexity = O(n)
