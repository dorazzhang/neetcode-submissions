class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # appear more than n/3 times

        # [5,2,3,2,2,2,2,5,5,5] n = 10 n/3 = 3

        # we can sort the string and walk through it (nlogn), 1
        # we can walk through and store freq in hashmap (o(n), o(n))
        # return keys with greater frequency

        # freq = defaultdict(int)

        # for num in nums:
        #     freq[num] += 1
        
        # target = len(nums) / 3
        # res = []

        # for key, val in freq.items():
        #     if val > target:
        #         res.append(key)
        
        # return res

        # we keep 2 candidate elements (max possible)
        # if there are ever 3 elements with same freq, we know we can remove all of them

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
            if len(freq) == 3:
                new_freq = defaultdict(int)
                for n in freq:
                    freq[n] -= 1
                    if freq[n] != 0:
                        new_freq[n] = freq[n]
                freq = new_freq
        
        res = []
        target = len(nums) // 3
        for n in freq:
            if nums.count(n) > target:
                res.append(n)
        
        return res