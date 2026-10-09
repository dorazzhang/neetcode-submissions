class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # empty dict

        for str in strs:
            sortedStrs = ''.join(sorted(str))
            result[sortedStrs].append(str) # 
        
        return list(result.values())
            
        