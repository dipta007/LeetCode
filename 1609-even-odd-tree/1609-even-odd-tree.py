# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        def call(curr, lvl):
            if curr is None:
                return
            
            if len(res) == lvl:
                res.append([])
            
            res[lvl].append(curr.val)
            call(curr.left, lvl+1)
            call(curr.right, lvl+1)

        call(root, 0)

        def check(row, increasing):
            if increasing:
                for v in row:
                    if v%2 == 0:
                        return False
                for a, b in zip(row, row[1:]):
                    if b <= a:
                        return False
            else:
                for v in row:
                    if v%2 == 1:
                        return False
                for a, b in zip(row, row[1:]):
                    if b >= a:
                        return False
            
            return True
        
        for i in range(len(res)):
            if check(res[i], i%2 == 0) == False:
                return False

        return True