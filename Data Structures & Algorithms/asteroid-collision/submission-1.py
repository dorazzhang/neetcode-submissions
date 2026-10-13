class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # asteroids in a row
        # indices represent position in space
        # abs val represents size
        # sign represents direction
        # moves at same speed

        # state of asteroids after all collisions
        # if two meet, smaller one explodes
        # same size, both explodes
        # moving in same direction will never meet

        # [2, 4, -4, -1]

        #  0->   1 -> <- 2  <- 3 
        #  0->   <- 3 
        #  0->

        # [0 1 2 3]

        # [0 1] # going right is ordered smallest to largest index
        # [3 2] # going left is order largest to smallest index

        #  0->   <-1   2->  <- 3 

        #[0 1 2 3]
        # 

        # have a stack that tracks most recent astroid going to the right
        # when you encounter one going to the left, if stack is empty do nothing
        # if stack has something, pop off of stack
        # compare them, continue popping until right wins or stack is empty
        # if right wins, push it back on the stack
        # if stack is empty, continue with next astroid

        right = []
        res = []

        for size in asteroids:
            if size > 0:
                right.append(size) # 2
                res.append(size) # 2 4
            elif size < 0 and right:
                while right and right[-1] < abs(size): # right astroids are being destoryed
                    right.pop()
                    res.pop()
                if not right:
                    res.append(size)
                elif right[-1] > abs(size):
                    continue
                else:
                    right.pop()
                    res.pop()
                    continue
            else:
                res.append(size)
        
        return res
                