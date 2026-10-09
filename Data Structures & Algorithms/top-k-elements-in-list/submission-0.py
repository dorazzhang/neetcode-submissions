class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        arr = []
        for num, freq in frequencies.items():
            arr.append([freq, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result

        
        