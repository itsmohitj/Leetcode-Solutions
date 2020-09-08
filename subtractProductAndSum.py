#Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productn=1
        sumn=0
        while(n>0):
            rem = n % 10
            productn *= rem
            sumn += rem
            n = n//10
        return productn-sumn

# Time Complexity = O(n)
# Space Complexity = O(1)
