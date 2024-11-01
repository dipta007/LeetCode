# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        def call(curr):
            if curr is None:
                return None
            
            nnode = TreeNode(curr.val)
            nnode.left = call(curr.left)
            nnode.right = call(curr.right)

            if curr.val in to_delete:
                nonlocal res
                if nnode.left:
                    res.append(nnode.left)
                if nnode.right:
                    res.append(nnode.right)
                return None
            
            return nnode
        
        nroot = call(root)
        if nroot: res.append(nroot)
        return res