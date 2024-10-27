class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y, a=0, b=0):
            return (x-a)*(x-a) + (y-b)*(y-b)
        
        points.sort(key=lambda x: dist(x[0], x[1]))
        return points[:k]