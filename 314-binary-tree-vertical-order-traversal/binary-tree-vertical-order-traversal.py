# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        res = defaultdict(dict)
        def call(curr, val, lvl):
            if curr:
                nonlocal res
                if lvl not in res[val]:
                    res[val][lvl] = []
                res[val][lvl].append(curr.val)
            
                call(curr.left, val - 1, lvl + 1)
                call(curr.right, val + 1, lvl + 1)
        
        call(root, 0, 0)

        ret = []
        for k in sorted(res.keys()):
            curr = []
            for k1 in sorted(res[k].keys()):
                curr.extend(res[k][k1])
            ret.append(curr)

        return ret