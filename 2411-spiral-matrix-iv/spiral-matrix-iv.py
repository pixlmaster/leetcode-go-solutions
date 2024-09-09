# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = []
        for i in range(m):
            mat.append([-1]*n)
    
        self.recurse(0,0,m-1,n-1,head,mat)
        return mat
        

    def recurse(self,startRow: int, startCol: int, row: int, col : int, head: ListNode, matrix: list[list[int]])-> None:
        """
        start from startrow,startcol, move till row, col , right, down,left, up and then recurse,
        """
        # print(matrix)
        # go right
        if startRow>row or startCol > col:
            return
        for c in range(startCol, col+1):
            if head:
                matrix[startRow][c] = head.val
                head = head.next
            else:
                return
        # go down
        for r in range(startRow+1, row+1):
            if head:
                matrix[r][col] = head.val
                head = head.next
            else:
                return
        # go left
        for c in range(col-1, startCol-1,-1):
            if head:
                matrix[row][c] = head.val
                head = head.next
            else:
                return
        
        # go up
        for r in range(row-1, startRow, -1):
            if head:
                matrix[r][startCol] = head.val
                head = head.next
            else:
                return 
        
        # recurse
        self.recurse(startRow+1, startCol+1, row-1, col -1 , head,matrix)
            
            