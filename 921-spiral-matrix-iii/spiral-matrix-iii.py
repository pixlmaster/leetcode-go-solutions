class Solution:
    left = "left"
    right = "right"
    up = "up"
    down = "down"
    nextMove = {
        down: left,
        left: up,
        up: right,
        right: down
    }

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        """
        store visited
        currMove = right
        nextMove = down -> left ->up -> right
        keep currMoving until next move is possible and mark visited
        """
        total = rows * cols
        visited = set()
        currMove = self.right

        ans = [[rStart, cStart]]
        visited.add((rStart,cStart))
        currRow = rStart
        currCol = cStart
        while len(ans) < total:
            currRow,currCol = self.makeMove(currRow,currCol,currMove)
            visited.add((currRow,currCol))
            if self.withinMatrix(currRow,currCol,rows,cols):
                ans.append([currRow,currCol])
            if self.isNextMovePossible(visited, self.nextMove[currMove], currRow, currCol):
                currMove = self.nextMove[currMove]

        return ans

    def makeMove(self, r: int, c: int, move: str) -> (int, int):
        if move == self.left:
            return r, c - 1
        elif move == self.right:
            return r, c+1
        elif move == self.up:
            return r-1, c
        else:
            return r+1,c

    def withinMatrix(self, r: int, c: int, row: int, col: int) -> bool:
        if 0 <= r < row and 0 <= c < col:
            return True
        else:
            return False

    def isNextMovePossible(self, visited , nextMove: str, r: int, c: int) -> bool:
        if nextMove == self.left:
            return (r,c-1) not in visited
        elif nextMove == self.right:
            return (r,c+1) not in visited
        elif nextMove == self.up:
            return (r-1,c) not in visited
        else:
            return (r+1,c) not in visited
