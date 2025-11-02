class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = 9, 9
        def check_row():
            for i in range(r):
                s = set()
                for j in range(c):
                    curr = board[i][j]
                    if curr == ".": continue
                    if curr in s:
                        return False
                    s.add(curr)
            return True
        
        def check_col():
            for i in range(c):
                s = set()
                for j in range(r):
                    curr = board[j][i]
                    if curr == ".": continue
                    if curr in s:
                        return False
                    s.add(curr)
            return True
        
        def check_square():
            for i in range(0, r, 3):
                for j in range(0, c, 3):
                    s = set()
                    for k in range(3):
                        for l in range(3):
                            curr = board[i+k][j+l]
                            if curr == ".": continue
                            if curr in s:
                                return False
                            s.add(curr)
            return True
        
        return check_row() and check_col() and check_square()



