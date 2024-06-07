class Point:
    def __init__(self, r: int, c : int):
        self.r = r
        self.c = c

class Solution:
    def totalNQueens(self, n: int) -> int:
        # place queen in a row up till n-1
            # place next queen in subsequent row
        placed = set()
        ans = 0
        for c in range(n):
            ans += self.placeQueens(0,c, n-1, n, placed)
                
        return ans
    
    def placeQueens(self,r : int,c :int, remaining : int, n: int, placed : set[Point]) -> int:
        if remaining == 0:
            return 1
        point = Point(r,c)
        placed.add(point)
        ans = 0
        for c in range(n):
            if self.checkValid(placed,r+1,c):
                ans+=self.placeQueens(r+1,c,remaining-1,n,placed)
        
        placed.remove(point)
        
        return ans
                
        

    def checkValid(self,queens : set[Point] , r : int, c: int) -> bool:
        for queen in queens:
            # check row
            if queen.r == r:
                return False
            # check col
            if queen.c == c:
                return False
            # check diagonals
            if queen.r - queen.c == r - c or queen.r + queen.c == r + c:
                return False
            
        return True