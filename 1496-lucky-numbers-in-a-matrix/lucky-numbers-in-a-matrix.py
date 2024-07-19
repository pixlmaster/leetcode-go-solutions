class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        row = len(matrix)
        col = len(matrix[0])
        ans =[]
        minRows = []
        for r in range(row):
            minRows.append(min(matrix[r]))

        for c in range(col):
            # for every col, iterate over the rows
            maxElem = 0
            maxRowIdx = -1
            for r in range(row):
                if matrix[r][c] > maxElem:
                    maxElem = matrix[r][c]
                    maxRowIdx = r
            
            if maxElem == minRows[maxRowIdx] :
                ans.append(maxElem)
        # print(minRows)
        return ans
