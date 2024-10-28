# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def call(curr, lvl):
            if not curr:
                return
            
            if len(res) == lvl:
                res.append([])
            
            res[lvl].append(curr.val)
            call(curr.left, lvl+1)
            call(curr.right, lvl+1)
        
        call(root, 0)
        return res