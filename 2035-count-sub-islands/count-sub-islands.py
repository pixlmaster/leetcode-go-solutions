class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        """
        1. traverse 2nd grid , find an island, all the island cells must have grid1 as [1]
        2. if any element does not have it continue visiting it but this is not a sub island nad mark the sub island as visited
        """
        ans = 0
        row = len(grid2)
        col = len(grid2[0])
        visited = []
        for r in range(row):
            visited.append([False] * col)
        for r in range(row):
            for c in range(col):
                if grid2[r][c] == 1 and not visited[r][c]:
                    if self.traverse(grid1, grid2, row, col, visited, r, c):
                        ans +=1
                    
        return ans

    def traverse(self, grid1: list[list[int]], grid2: list[list[int]], row: int, col: int, visited: list[list[bool]],
                 r: int, c: int) -> bool:
        if r < 0 or r >= row or c < 0 or c >= col or grid2[r][c] == 0 or visited[r][c]:
            return True
        
        visited[r][c] = True
        
        # visit top
        top = self.traverse(grid1, grid2, row, col, visited,r-1,c)
        
        # visit left
        left = self.traverse(grid1, grid2, row, col, visited,r,c-1)
        
        # visit bottom 
        bottom = self.traverse(grid1, grid2, row, col, visited,r+1,c)
        
        # visit right
        right = self.traverse(grid1, grid2, row, col, visited,r,c+1)
        
        if grid1[r][c] == 0:
            return False
        
        return top and left and bottom and right
