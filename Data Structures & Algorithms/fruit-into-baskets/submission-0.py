class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits[i] is type of fruit ith tree produces

        # want as much fruit as possible under following rules

        # only two baskets -> hold single type of fruit no capapcity
        #starting from any tree, must pick one fruit from every tree & must fit in one of baskets

        # once you reach a tree w fruit that cant fit, stop

        #return max number of fruits

        # brute force approach: try every starting point and count the number of fruits that it yields and store global max
        # O(n^2) time O(1) space

        # maintain a valid sliding window
        # increment right while valid
        # increment left while not valid
        # hashmap storing fruits in window -> if length becomes 3, its invalid, we increment left until one of the counts goes back to 0, del that entry

        fruitMap = defaultdict(int) #0's
        l = 0
        r = 0
        res = 0

        while r < len(fruits) and l < len(fruits):
            fruitMap[fruits[r]] += 1

            if len(fruitMap) > 2:
                res = max(res, r - l)

            while l < len(fruits) and len(fruitMap) > 2:
                fruitMap[fruits[l]] -= 1
                if fruitMap[fruits[l]] == 0:
                    del fruitMap[fruits[l]]
                l += 1        

            r += 1
        
        return max(res, r - l)