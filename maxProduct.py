"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]-1) * (nums[1]-1)

# Time Complexity = O(nlogn)
# Space Complexity = O(1)

# There is another solution which have time complexity O(n) but surprisingly it was taking more time on leetcode when submitting.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nlargest = max(nums)
        nums.remove(nlargest)
        return (nlargest-1) * (max(nums)-1)
