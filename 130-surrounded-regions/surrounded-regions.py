class Solution:
    o = "O"
    x = "X"
    a = "a"
    v = "v"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # iterate over grid
        #   if elem is 0
        #       visit the region
        #       if any region reaches the edge
        #           do not modify anything
        #       else modify to a third character
        #       second pass modify third character to x


        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if board[r][c] == self.o:
                    shouldflip = not self.visit(board,r,c)


                    if shouldflip:
                        self.mark(board,r,c,self.a)
                    else:
                        self.mark(board,r,c,self.o)


        for r in range(row):
            for c in range(col):
                if board[r][c] == self.a:
                    board[r][c] = self.x
    
    def visit(self,board,r,c) -> bool:
        row = len(board)
        col = len(board[0])

        if r<0 or r>=row or c<0 or c>=col:
            return True
        if board[r][c] != self.o :
            return False

        board[r][c] = self.v

        return self.visit(board,r-1,c) or self.visit(board,r+1,c) or self.visit(board,r,c-1) or self.visit(board,r,c+1)
        

    def mark(self,board,r,c, char):
        row = len(board)
        col = len(board[0])

        if r<0 or r>=row or c<0 or c>=col:
            return 

        if board[r][c] != self.v :
            return 

        board[r][c] = char

        self.mark(board,r-1,c,char)
        self.mark(board,r+1,c,char)
        self.mark(board,r,c-1,char)
        self.mark(board,r,c+1,char)
        