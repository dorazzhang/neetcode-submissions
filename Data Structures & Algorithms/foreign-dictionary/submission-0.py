class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = [[] for _ in range(26)]

        # char - ord(a) so that a is 0, b is 1, etc

        prev = words[0]
        for w in range(1, len(words)):
            minLen = min(len(prev), len(words[w]))
            difference = False
            for c in range(minLen):
                if prev[c] != words[w][c]:
                    adj[ord(prev[c]) - ord('a')].append(ord(words[w][c]) - ord('a'))
                    difference = True
                    break
            if not difference and len(prev) > len(words[w]):
                return ""
            prev = words[w]
    

        res = []
        state = [0] * 26
        def dfs(letter):
            # cycle
            if state[letter] == 1:
                return False
            if state[letter] == 2:
                return True
            state[letter] = 1

            for neighbor in adj[letter]:
                if not dfs(neighbor):
                    return False
            
            state[letter] = 2
            res.append(chr(letter + ord('a')))

            return True
        
        seenLetters = set()

        for word in words:
            for char in word:
                seenLetters.add(ord(char) - ord('a'))
        
        for letter in seenLetters:
            if not dfs(letter):
                return ""
        
        res.reverse()

        return "".join(res)