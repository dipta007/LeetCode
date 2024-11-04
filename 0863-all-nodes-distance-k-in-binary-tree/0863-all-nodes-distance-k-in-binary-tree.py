# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        from collections import defaultdict
        adj = defaultdict(list)
        def make_graph(curr, par):
            if curr is None:
                return

            if curr and par:
                nonlocal adj
                adj[curr.val].append(par.val)
                adj[par.val].append(curr.val)

            make_graph(curr.left, curr)
            make_graph(curr.right, curr)

        make_graph(root, None)

        from collections import deque
        dq = deque()

        dq.append(target.val)
        vis = [-1] * 100000
        vis[target.val] = 0
        while dq:
            u = dq.popleft()

            for v in adj[u]:
                if vis[v] == -1:
                    dq.append(v)
                    vis[v] = vis[u] + 1
        
        return [v for v in range(10000) if vis[v] == k]