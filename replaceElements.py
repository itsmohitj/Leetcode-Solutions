"""Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = mx
            if temp > mx:
                mx = temp
        return arr

# Time Complexity = O(n)
# Space Complexity = O(1)
