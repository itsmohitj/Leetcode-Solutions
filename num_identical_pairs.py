# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 1
        nums.sort()
        current = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if nums[i] == current:
                count +=1
            else:
                res += (count*(count-1)) // 2
                count = 1
                current = nums[i]
        return res+(count*(count-1)) // 2


# Time Complexity = O(n)
# Space Complexity = O(1)
