# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(lft, rgt, curr):
            if curr is None:
                return True

            if curr.val < lft or curr.val > rgt:
                return False
            
            return check(lft, curr.val-1, curr.left) and check(curr.val+1, rgt, curr.right)

        # return check(-int(2147483655), int(2147483655), root)

        res = True
        def call(curr):
            if not curr:
                return -9e11, 9e11

            lft = call(curr.left)
            rgt = call(curr.right)
            if (lft[1] != 9e11 and lft[1] >= curr.val) or (rgt[1] != 9e11 and rgt[0] <= curr.val):
                print(curr.val)
                nonlocal res
                res = False

            a, b = lft[0], rgt[1]
            if abs(a) == 9e11:
                a = curr.val
            if abs(b) == 9e11:
                b = curr.val
            return a, b

        call(root)
        return res