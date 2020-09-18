"""
Given an unsorted integer array, find the smallest missing positive integer.

Input: [1,2,0]
Output: 3
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(1,abs(max(nums))+2):
            if i not in nums:
                return i

# Time Complexity = O(n)
# Space Complexity = O(1)
