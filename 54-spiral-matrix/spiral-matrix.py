class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        return self.getSpiralList(matrix,0,row-1,0,col-1)
        
    def getSpiralList(self, matrix: List[List[int]], srow : int, erow: int, scol:int, ecol: int ) -> List[int]:
        if srow> erow or scol >ecol:
            return []
        

        slist = []
        
        # traverse right
        for j in range(scol,ecol+1):
            slist.append(matrix[srow][j])
        # print(slist)

        # traverse bottom
        for i in range(srow+1,erow+1):
            slist.append(matrix[i][ecol])
        # print(slist)

        if srow < erow:
            # traverse left
            for j in range(ecol-1,scol-1,-1):
                slist.append(matrix[erow][j])
        # print(slist)

        if scol < ecol :
        # traverse up
            for i in range(erow-1,srow,-1):
                slist.append(matrix[i][scol])

        # print(slist)
        slist.extend(self.getSpiralList(matrix,srow+1,erow-1, scol+1, ecol-1))
        return slist
        