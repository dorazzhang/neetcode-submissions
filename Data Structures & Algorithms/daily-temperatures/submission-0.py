class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given array of ints where each is the daily temp on a day
        # return array where i is the number of days after the ith day where there's a warmer temp

        # brute force solutions: nested for loops
        
        # sort the temperatures as tuples, but then you would still have to check which temps are the closest days after

        # loop in reverse and add the max seen temp to a stack with its index number
        # when encountering temperatures, pop off the stack and check if its greater
        # but then if its 25 26 40 itll keep 40 even though 26 works too
        # add elements to a stack as long as they are constantly decreasing
        # once we reach a larger element, we pop off the stack until its empty or the element is not smaller
        # initialize result array with zeros

        res = [0] * len(temperatures)
        stack = []
        prev = temperatures[0]
        stack.append(0)
        for i in range(1, len(temperatures)):
            if stack and temperatures[i] >= prev:
                peek = stack[-1]
                while stack and temperatures[peek] < temperatures[i]:
                    res[peek] = i - peek
                    stack.pop()
                    if stack:
                        peek = stack[-1]
            stack.append(i)
            prev = temperatures[i]
        return res



        