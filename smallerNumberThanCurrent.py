#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

#Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash = {}
        sortednums= sorted(nums)
        for index,value in enumerate(sortednums):
            if value not in hash:
                hash[value] = index
        return [hash[k] for k in nums]

# Time Complexity = O(nlogn) {Due to sorting}
# Space Complexity = O(n)
