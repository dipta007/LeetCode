# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = {}
        def call(curr, row, col):
            if not curr:
                return
            
            if col not in values: values[col] = {}
            if row not in values[col]: values[col][row] = []

            values[col][row].append(curr.val)

            call(curr.left, row+1, col-1)
            call(curr.right, row+1, col+1)

        call(root, 0, 0)

        for c, cval in values.items():
            for r in values[c].keys():
                values[c][r] = list(sorted(values[c][r]))
        
        res = []
        for c in sorted(values.keys()):
            curr = []
            for r in sorted(values[c].keys()):
                curr.extend(values[c][r])
            res.append(curr)
        
        return res