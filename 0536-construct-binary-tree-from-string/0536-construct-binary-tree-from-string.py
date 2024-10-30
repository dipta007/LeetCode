# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def call(l, r):
            l += 1
            r -= 1
            if l > r:
                return None

            node_val = ""
            p_start = -1
            for i in range(l, r+1):
                if s[i] == '(':
                    p_start = i
                    break
                
                node_val += s[i]
            
            node_val = int(node_val)
            curr_node = TreeNode(node_val)
            if p_start != -1:
                p = 0
                for p_end in range(p_start, r+1):
                    if s[p_end] == '(':
                        p += 1
                    elif s[p_end] == ')':
                        p -= 1
                    
                    if p == 0:
                        break
            
                curr_node.left = call(p_start, p_end)
                curr_node.right = call(p_end+1, r)

            return curr_node
        
        return call(-1, len(s))

