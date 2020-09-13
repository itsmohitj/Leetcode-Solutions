"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Input: 701
Output: "ZY"
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while(n>0):
            n -= 1
            res = chr(n%26+65) + res
            n //= 26
        return res

# Time Complexity = O(n)
# Space Complexity = O(1)
