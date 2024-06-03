class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isFirstRow = False
        isFirstCol  = False
        row= len(matrix)
        col = len(matrix[0])
        for c in range(0,col):
            if matrix[0][c] == 0:
                isFirstRow = True

        for r in range(0,row):
            if matrix[r][0] == 0:
                isFirstCol = True



        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        print(matrix)

        for c in range(1,col):
            if matrix[0][c] == 0:
                for r in range(1,row):
                    matrix[r][c] = 0

        for r in range(1,row):
            if matrix[r][0] == 0:
                for c in range(1,col):
                    matrix[r][c] = 0
        
        if isFirstCol:
            for r in range(0,row):
                 matrix[r][0] = 0

        if isFirstRow:
            for c in range(0,col):
                 matrix[0][c] = 0





        """
        Do not return anything, modify matrix in-place instead.
        """
        