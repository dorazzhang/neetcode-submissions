class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # 1. first differing char
        # 2. prefixes come before

        orderInd = { c : i for i, c in enumerate(order)} # maps char to its index / ith spot in the dictionary

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False # w2 is a prefix of w1 WRONG ORDER
                if w1[j] != w2[j]:
                    if orderInd[w1[j]] > orderInd[w2[j]]: # w1 letter comes after w2 letter in alphabet
                        return False
                    break
        
        return True
                