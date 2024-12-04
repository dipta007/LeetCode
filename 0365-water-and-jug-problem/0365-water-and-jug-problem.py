class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        vis = [[0] * (y+4) for _ in range(x+4)]
        
        def call(j1, j2):
            if j1 + j2 == target:
                return True

            # print(j1, j2)
            if vis[j1][j2]:
                return False
            
            vis[j1][j2] = 1

            ret = False
            ret = ret or call(x, j2)
            ret = ret or call(j1, y)

            ret = ret or call(0, j2)
            ret = ret or call(j1, 0)

            pour_to_1 = min(x-j1, j2)
            ret = ret or call(j1+pour_to_1, j2-pour_to_1)

            pour_to_2 = min(j1, y-j2)
            ret = ret or call(j1-pour_to_2, j2+pour_to_2)

            return ret

        return call(0, 0)