# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def call(curr, lvl):
            if curr:
                if len(res) < lvl:
                    res.append(curr.val)

                call(curr.right, lvl+1)
                call(curr.left, lvl+1)

        call(root, 1)
        return res

        