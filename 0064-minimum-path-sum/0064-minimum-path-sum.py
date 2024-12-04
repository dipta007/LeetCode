class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def call(x, y):
            if x == len(grid)-1 and y == len(grid[0])-1:
                return grid[x][y]

            if x > len(grid)-1 or y > len(grid[0])-1:
                return 100000000000000

            return min(call(x+1, y), call(x, y+1)) + grid[x][y]
        
        return call(0, 0)