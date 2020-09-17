"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash = {}
        res = []
        for i in nums:
            hash[i] = hash.get(i,0) + 1
        for key,val in hash.items():
            if val == 1:
                res.append(key)
        return res

# Time Complexity = O(n)
# Space Complexity = O(n)
