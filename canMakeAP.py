"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.


Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        a = min(arr)
        l = max(arr)

        sumap = n/2* (a + l)
        if sum(arr) == sumap:
            return True
        return False

# Time Complexity = O(n)
# Space Complexity = O(1)
