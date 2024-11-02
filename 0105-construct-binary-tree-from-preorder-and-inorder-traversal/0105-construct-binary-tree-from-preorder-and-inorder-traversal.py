# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_ind = 0
        ino_ind = {v: i for i, v in enumerate(inorder)}

        root = TreeNode()

        def call(l, r):
            if l > r:
                return None

            nonlocal pre_ind
            curr_root = preorder[pre_ind]
            pre_ind += 1

            ind_in_inorder = ino_ind[curr_root]

            curr = TreeNode(inorder[ind_in_inorder])
            curr.left = call(l, ind_in_inorder-1)
            curr.right = call(ind_in_inorder+1, r)

            return curr
        
        return call(0, len(inorder)-1)
