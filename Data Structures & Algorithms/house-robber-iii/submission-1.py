# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # entrnace to area is root
        # each house has only one parent house
        # binary tree
        # contact police if two directly linked house were broken
        # max money thief robs without alerting police

        # robber either robs or doesnt rob a house
        # if he doesnt rob it, hes free to do whatever later
        # if he robs it, he couldnt rob the one before

        # kind of like dp on a tree
        # base case is zero houses robbed = 0 dollars
        # how do u do dp on a tree lol

        def dfs(root):
            if not root:
                return [0,0] # with or without root
            left = dfs(root.left)
            right = dfs(root.right)

            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left[0], left[1]) + max(right[0], right[1])

            return [withRoot, withoutRoot]
        
        res = dfs(root)
        return max(res)
            
