class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people where people[i] is weight of ith person
        # infinite number of boats
        # max weight of limit
        # at most two ppl, sum of weights <= limit

        # minimum # of boats to carry every person

        # [1,3,2,3,2]
        # sorted?
        # [1,2,2,3,3] try to pair people if possible
        # (1, 3) > sum
        # increment count, decrement right
        # (1, 3)
        # increment count, decrement right
        # (1, 2)
        # increment count, increment left
        # (2)

        # what if sum is too small, does it matter?

        people.sort()

        r = len(people) - 1
        l = 0
        boats = 0

        while l <= r:
            weight = people[r] + people[l]
            if weight > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            boats += 1
        
        return boats