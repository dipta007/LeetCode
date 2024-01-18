class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        user_visited = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visited[u].append((t, w))
        
        for k in user_visited.keys():
            user_visited[k].sort(key=lambda x: x[0])
            user_visited[k] = [x[1] for x in user_visited[k]]

        mx = -1
        res = []

        # print(user_visited)

        def smaller(x, y, z, res):
            nw = " ".join([x, y, z])
            prev = " ".join(res)

            print(nw, prev, len(nw) < len(prev), nw < prev)
            return nw < prev
            return len(nw) < len(prev) or nw < prev

        for k, v in user_visited.items():
            if len(v) >= 3:
                vl = len(v)
                for i in range(vl):
                    for j in range(i+1, vl):
                        for k in range(j+1, vl):
                            x, y, z = v[i], v[j], v[k]

                            cnt = 0
                            for k1, v1 in user_visited.items():
                                v1l = len(v1)
                                if len(v1) >= 3:
                                    flg = 0
                                    for i1 in range(v1l):
                                        for j1 in range(i1+1, v1l):
                                            for k1 in range(j1+1, v1l):
                                                x1, y1, z1 = v1[i1], v1[j1], v1[k1]
                                                
                                                if x == x1 and y == y1 and z == z1:
                                                    flg += 1
                                    if flg:
                                        cnt += 1
                                
                            # print(cnt, mx, x, y, z)
                            if cnt > mx:
                                mx = cnt
                                res = [x, y, z]
                            elif cnt == mx and smaller(x, y, z, res):
                                res = [x, y, z]
        return res
