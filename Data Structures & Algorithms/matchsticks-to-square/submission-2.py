class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # length of ith stick
        # use all to make a square
        # true if can make, false if not

        # need four groups of matchsticks with the same sum

        # must use all of them as well

        # [1,3,4,2,2,4]

        # target sum is then the sum of all matchsticks / 4
        # if not divisible, also false

        total = sum(matchsticks)

        if len(matchsticks) < 4 or (total % 4) != 0:
            return False
        
        target = total // 4

        # easiest way is to sort them so if sum is less than target we can increment, nevermind this doesnt work

        matchsticks.sort(key=None, reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]

                    if dfs(i + 1):
                        return True
                    sides[side] -=  matchsticks[i]
                if sides[side] == 0:
                    break
            return False
        
        # basically for every matchstick, try a scenerio where you add it to one of the four sides
        # explore every possible combination
        # if any of them return True (when all matches were placed and sides were equal), then its true

        return dfs(0)
