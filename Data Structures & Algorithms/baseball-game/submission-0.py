class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        score = []
        for op in operations:
            if op == 'D':
                res = score[-1] * 2
                score.append(res)
                sum += res
            elif op == 'C':
                res = score[-1]
                score.pop()
                sum -= res
            elif op == '+':
                res = score[-1] + score[-2]
                score.append(res)
                sum += res
            else:
                res = int(op)
                score.append(res)
                sum += res
        return sum
            
        