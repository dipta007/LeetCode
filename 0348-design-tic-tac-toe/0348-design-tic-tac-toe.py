class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.b = [[-1 for _ in range(n)] for __ in range(n)]
        
    def check(self):
        for i in range(self.n):
            val = self.b[i][0]
            if val == -1: continue
            same = True
            for j in range(self.n):
                if self.b[i][j] != val:
                    same = False
                    break
            if same:
                return val
        
        for i in range(self.n):
            val = self.b[0][i]
            if val == -1: continue
            same = True
            for j in range(self.n):
                if self.b[j][i] != val:
                    same = False
                    break
            if same:
                return val
            
        i, j = 0, 0
        val = self.b[0][0]
        same = True
        while i < self.n:
            if self.b[i][j] != val:
                same = False
                break
            i += 1
            j += 1
        if same and val != -1:
            return val
        
        i, j = 0, self.n-1
        val = self.b[0][self.n-1]
        same = True
        while i < self.n:
            if self.b[i][j] != val:
                same = False
                break
            i += 1
            j -= 1
        if same and val != -1:
            return val
        
        return -1

    def move(self, row: int, col: int, player: int) -> int:
        self.b[row][col] = player
        win = self.check()
        if win == -1: win = 0
        return win
            

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)