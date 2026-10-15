class Solution:
    def decodeString(self, s: str) -> str:
        # k[encoded] where encoded string inside is being repeated k times
        # "2[a3[b]]c"
        # "2[abbb]c"
        # "abbbabbbc"
        # axb3[z]4[c]


        # 2[a3[b]]c

        # 2[a3[b]]

        # a3[b]a3[b]c
        # sliding window? to find encoded parts that need to be decoded
        # 2[a3[b]]c (LIFO)
        # 2 [ a 3 [ b ] <- see a closing bracket
        # then we pop until we get to a number
        # 3[b] -> bbb push this back into stack
        # 2 [ a b b b
        # continue pushing
        # 2 [ a b b b ] <- see another closing bracket
        # 2[abbb] -> abbbabbb
        # abbbabbb c -> once we reach end of string we return our stack as a string

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                encode = ""
                digit = ""
                while stack and stack[-1] != "[":
                    encode += stack.pop()
                encode = encode[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit += stack.pop()
                digit = int(digit[::-1])

                for i in range(digit):
                    for e in encode:
                        stack.append(e)
        
        return "".join(stack)





