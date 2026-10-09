class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    stack.append(x + y)
                elif t == "*":
                    stack.append(x * y)
                elif t == "-":
                    stack.append(x - y)
                else:
                    stack.append(int(x / y))
        return stack[0]
                
                
        