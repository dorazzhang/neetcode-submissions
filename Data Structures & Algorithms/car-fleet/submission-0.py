class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars going one way
        # position, speed of each car
        # destination at target
        # car can't pass another car, can only catch up and drive same speed
        # car fleet non-empty set of cars at same pos and speed
        
        # for every speed, position you add speed to position incrementally
        # when any position equals another, that positions speed changes to match the one in front

        # if a car reaches the end before or same as the car in front does with their initial speeds, that means they became a fleet

        cars = [[position[i], speed[i]] for i in range(0, len(position))]

        stack = []
        for p, s in sorted(cars)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)




        