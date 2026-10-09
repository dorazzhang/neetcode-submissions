class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs: # for every word
            result.append(str(len(s))) # append length of word to know how long word is
            result.append("#") # append seperator to know which characters are length
            result.append(s) # append word
        return "".join(result)
            


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s): # count i to go through string
            j = i # j to store end of lengths / words
            while s[j] != '#': # while its not # its the length
                j += 1 # increment j to end of length
            length = int(s[i:j])
            i = j + 1 # move i to start of word
            j = j + length + 1 # move j to end of word
            result.append(s[i:j]) # append entire word
            i = j # move i to end of word
        return result
        
                

