"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Input: low = 100, high = 300
Output: [123,234]
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for num in range(1,9):
            while num <= high and num % 10 != 0:
                if num >= low:
                    res.append(num)
                num = (num * 10) + (num % 10) + 1
        return sorted(res)

# Time Complexity = O(nlogn)
# Space Complexity = O(n)
