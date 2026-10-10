class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n gas stations along circular route

        # given gas[i] and cost[i] where = amt of gas at ith station and amt needed to get to i+1th

        # begin with empty tank at one gas station

        # return which index such that you can travel around circuit once in clockwise direction

        # [-1, 0, -1, 3] <- amount of gas in tank after getting to next station, if negative needed previously to arriving at this station

        # [-1, -1, 1]

        if sum(gas) < sum(cost):
            return -1
        
        curr_gas = 0
        res = 0
        
        for i in range(len(gas)):

            curr_gas += (gas[i] - cost[i])

            if curr_gas < 0:
                curr_gas = 0
                res = i + 1
            
        return res