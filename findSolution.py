"""
Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this: 
   
interface CustomFunction {
    public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
        int f(int x, int y);
};


For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.

You may return the solutions in any order.

Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: function_id = 1 means that f(x, y) = x + y

"""

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x,y = 1, z
        res = []
        while 1<= x <=1000 and 1<=y<=1000:
            if customfunction.f(x,y) == z:
                res.append([x,y])
                x += 1
                y -= 1
            elif customfunction.f(x,y) < z:
                x += 1
            else:
                y -= 1
        return res

# Time Complexity = O(x+y)
# Space Complexity = O(n) where n is the length of the list returned by this function.
