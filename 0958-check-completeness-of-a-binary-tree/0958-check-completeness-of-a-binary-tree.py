# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        from collections import defaultdict
        done_lvl = defaultdict(int)
        cnt = defaultdict(int)

        def call(curr, lvl):
            if curr is None:
                done_lvl[lvl] = 1
                return True
            
            if done_lvl[lvl]:
                return False
            cnt[lvl] += 1
            
            res = True
            return call(curr.left, lvl+1) and call(curr.right, lvl+1)

        if call(root, 0) == False:
            return False
        mx_lvl = max(cnt.keys())
        return all(done_lvl[i] == 0 for i in range(mx_lvl))