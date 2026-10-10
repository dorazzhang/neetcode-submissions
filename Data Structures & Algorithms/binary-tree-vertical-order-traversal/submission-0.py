# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # bfs but start at 0 and when you go left you decrement by 1 and when you go right you increment by 1 
        # at each node, store the nodes and their value

        # [(3, 0) (9, -1) (20, 1) (15, 0) (7, 2)]
        # then sort with stable sort and return
        # O(n) time and space
        if not root:
            return []
        nodes = []
        queue = deque()
        queue.append((root, 0))
        nodes.append((root.val, 0))

        while queue:
            node, val = queue.popleft()
            if node.left:
                queue.append((node.left, val - 1))
                nodes.append((node.left.val, val - 1))
            if node.right:
                queue.append((node.right, val + 1))
                nodes.append((node.right.val, val + 1))
        

        nodes.sort(key = lambda x : x[1])

        res = []
        curr = []
        prev_val = nodes[0][1]
        for node, val in nodes:
            if prev_val == val:
                curr.append(node)
            else:
                res.append(curr)
                curr = []
                prev_val = val
                curr.append(node)
        if curr != []:
          res.append(curr)  
        return res

