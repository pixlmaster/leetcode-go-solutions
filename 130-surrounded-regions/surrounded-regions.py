class Solution:
    o = "O"
    x = "X"
    a = "a"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = len(board)
        col = len(board[0])

        for r in range(row):
            self.visit(board,r,0)
            self.visit(board,r,col-1)
        for c in range(col):
            self.visit(board,0,c)
            self.visit(board,row-1,c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == self.a:
                    board[r][c] = self.o
                else:
                    board[r][c] = self.x
    
    def visit(self,board,r,c) -> None:
        row = len(board)
        col = len(board[0])

        if r<0 or r>=row or c<0 or c>=col or board[r][c] != self.o:
            return

        board[r][c] = self.a

        self.visit(board,r-1,c)
        self.visit(board,r+1,c)
        self.visit(board,r,c-1)
        self.visit(board,r,c+1)
        

        