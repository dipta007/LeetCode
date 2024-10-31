class TicTacToe:

    def __init__(self, n: int):
        self.mat = [[0] * n for _ in range(n)]
        self.r, self.c = len(self.mat), len(self.mat[0])

    def move(self, row: int, col: int, player: int) -> int:
        def win():
            win = True
            for i in range(self.c):
                if self.mat[row][i] != player:
                    win = False
            if win: return True

            win = True
            for i in range(self.r):
                if self.mat[i][col] != player:
                    win = False
            if win: return True

            if row - col == 0:
                cnt = 0
                i, j = 0, 0
                while i < self.r and j < self.c:
                    cnt += int(self.mat[i][j] == player)
                    i += 1
                    j += 1
            
                if cnt == self.r:
                    return True

            if row == self.r - col - 1:
                cnt = 0
                i, j = 0, self.r-1
                while i < self.r and j >= 0:
                    cnt += int(self.mat[i][j] == player)
                    i += 1
                    j -= 1
                print("+", cnt, row, col, player)
                if cnt == self.r:
                    return True

            return False

        self.mat[row][col] = player
        if win(): return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)