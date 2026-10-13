# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # binary search tree, all nodes are unique
        # two nodes p and q from the tree
        # return lowest common ancestor of the two nodes
        # the lowest node in a tree where both p and q are descendants
        # ancestor is allowed to be descendant of itself

        # while true loop
        # check if p <= root <= q or vise versa
        # then return node
        # else if both greater, node = node.right
        # else, node = node.left

        node = root

        while True:
            if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
                return node
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                node = node.right
            