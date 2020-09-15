"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lis = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        return max(lis)

# Time Complexity = O(n^2)
# Space Complexity = O(n)
