class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        adj = defaultdict(list)
        indeg = [0] * (numCourses + 4)
        for x, y in prerequisites:
            adj[y].append(x)
            indeg[x] += 1
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        while len(q) > 0:
            u = q.popleft()
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return all([indeg[i] == 0 for i in range(numCourses)])