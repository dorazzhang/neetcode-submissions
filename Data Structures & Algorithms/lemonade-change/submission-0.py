class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # customer gives 5, 10, 20
        # we give 0, 5, or 10 + 5 dollars back
        # note: if you have two 10's and need to give a customer five, that doesn't work
        # always give away 10's before 5's

        change = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 10:
                if change[5] >= 1:
                    change[5] -= 1
                else:
                    return False
            elif bill == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            change[bill] += 1
        return True
                 
        