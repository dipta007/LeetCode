# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_ind = len(postorder) - 1
        in_to_ind = {v: i for i, v in enumerate(inorder)}

        def call(l, r):
            if l > r:
                return None

            nonlocal post_ind
            curr_root = postorder[post_ind]
            post_ind -= 1

            inorder_ind = in_to_ind[curr_root]

            curr = TreeNode(inorder[inorder_ind])
            curr.right = call(inorder_ind+1, r)
            curr.left = call(l, inorder_ind-1)

            return curr
        
        return call(0, len(postorder)-1)