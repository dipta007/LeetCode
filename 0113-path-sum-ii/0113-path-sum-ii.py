# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []
        def is_leaf(curr):
            return not curr.left and not curr.right

        def call(curr, cum, cumL):
            if not curr:
                return
            
            if cum + curr.val == target and is_leaf(curr):
                nonlocal res
                res.append(cumL[:] + [curr.val])
                return
            
            call(curr.left, cum+curr.val, cumL + [curr.val])
            call(curr.right, cum+curr.val, cumL + [curr.val])

        call(root, 0, [])
        return res