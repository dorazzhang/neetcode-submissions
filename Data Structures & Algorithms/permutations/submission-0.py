class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [] -> None
        # 1 -> 1
        # 1 2 -> 1 2, 2 1
        # 1 2 3 -> 3 1 2, 1 3 2, 1 2 3, 3 2 1, 2 3 1, 2 1 3

        perms = [[]]

        for num in nums:
            additional_perms = []
            for perm in perms:
                for i in range(len(perm) + 1): # can insert from 0 to right after perms
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num) # insert num at index i
                    additional_perms.append(perm_copy)
            perms = additional_perms
        
        return perms

