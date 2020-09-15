"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        currentSum = 0
        maxSum = arr[0]
        for i in range(len(arr)):
            currentSum += arr[i]
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum

# Time Complexity = O(n)
# Space Complexity = O(1)
