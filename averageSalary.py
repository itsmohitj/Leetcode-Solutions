"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) -min(salary)) / (len(salary) - 2)

# Time Complexity = O(n)
# Space Complexity = O(1)
