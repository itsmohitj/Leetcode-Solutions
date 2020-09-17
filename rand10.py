"""
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

What is the expected value for the number of calls to rand7() function?

Input: n = 3
Output: [3,8,10]
"""


# Solution

# 1.Generate a from 1 to 7 and b from 1 to 7, then we have 7x7 = 49 options.Let us create number c = (a-1)*7 + b-1, then we can show that c is number between 0 and 48.
# 2. Now, let us divide these number into groups: [0,9]; [10;19]; [20;29]; [30;39]; [40;48]. If we get into one of the first four group, then there is ten number in each group, so we just return c%10 + 1.
# 3.If we are in the fifth group,there are only 9 numbers in this group and we need 10, use of 9 is not fair for generatinh 10 numbers. So in these case, we say, that our experiment was not working, and we just start it all over again!.
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7()-1)*7 + (rand7()-1)
        return self.rand10() if num >= 40 else (num%10)+1

# Expected Number of calls : What we do here is called sampling with rejection. Success of first sampling is p = 40/49. If first time our sampling was not working and it worked second time we have (1-p)*p, if it worked third time it is (1-p)*(1-p)*p and so on.Each time we use two rand7() generation. So, overall our expectation is 2*p + 4*(1-p)*p + 6*(1-p)^2*p + ... Note, that it is nothing else than geometrical distribution:  so the answer is just 2/p = 98/40 = 2.45.
# Time Complexity = O(1) average, but O(infinity) for worst case.
# Space Complexity = O(1)
