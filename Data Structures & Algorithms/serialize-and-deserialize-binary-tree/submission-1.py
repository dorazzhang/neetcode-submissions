# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # do something with bfs and process nodes topologically
        # so like 1 2 3 null null 4 5
        # can store the value and a diving character in between like #
        # so 1#2#3#x

        queue = deque()
        queue.append(root)
        res = []

        while queue:
                node = queue.popleft()
                if not node:
                    res.append('x')
                    res.append('#')
                    continue
                
                res.append(str(node.val))
                res.append('#')
                queue.append(node.left)
                queue.append(node.right)
            
        return "".join(res)[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # "1#2#3#x#x#4#5#x#x#x#x"
        data = data.split("#")
        # [1, 2, 3, x, x, 4, 5, x, x, x, x]

        if data[0] == 'x':
            return None
        
        queue = deque()
        root = TreeNode()
        root.val = int(data[0])

        queue.append(root)
        n = 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                left_val = data[n]
                right_val = data[n + 1]

                left = None if left_val == 'x' else TreeNode()
                if left:
                    left.val = int(left_val)

                right = None if right_val == 'x' else TreeNode()
                if right:
                    right.val = int(right_val)
                
                node.left = left
                node.right = right

                if left:
                    queue.append(left)
                if right:
                    queue.append(right)

                n += 2
        
        return root

