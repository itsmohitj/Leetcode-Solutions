"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if abs(arr[i]-arr[j]) <=a:
                    for k in range(j+1,n):
                        if abs(arr[k]-arr[j]) <=b and abs(arr[i]-arr[k]) <=c:
                            count += 1
        return count

# Time Complexity = O(n^3) (Although time complexity is in cubic, this solution was faster than 94.39% of python3 submissions at the time of submission).
# Space Complexity = o(1)