class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        """
        1. create a matrix, initiliase mat[0][c] as colSUM[c]
        2. for row in ROWS:
            currSUM = sum(mat[row])
            currCOL = 0
            while currSUM != rowSUM[row]:
                if currSum - mat[row][currCol] > rowSum[row]
                    mat[row+1][currCol] = mat[row][currCol]
                    currSum = currSum - mat[row][currCol]
                else:
                    mat[row+1][currCol] = rowSum[row] - mat[row][currCol]
                    currSum = rowSum[row]
        3. return mat
        """
        ans = []
        row = len(rowSum)
        col = len(colSum)
        for r in range(row):
            temp = [0]*col
            ans.append(temp)
        for c in range(col):
            ans[0][c] = colSum[c]
        # print(ans)
        for r in range(row):
            currSum = sum(ans[r])
            targetSum = rowSum[r]
            currCol = 0
            while r < row -1 and currSum != targetSum:
                # print(currSum, r, currCol)
                if currSum - ans[r][currCol] > targetSum:
                    ans[r+1][currCol] = ans[r][currCol]
                    currSum = currSum - ans[r][currCol]
                    ans[r][currCol] = 0
                    currCol += 1
                elif currSum - ans[r][currCol] <= targetSum:
                    ans[r+1][currCol] = currSum - targetSum
                    ans[r][currCol] = ans[r][currCol] - (currSum - targetSum)
                    currSum = targetSum
                    currCol += 1
                # print("ans", ans)
        return ans