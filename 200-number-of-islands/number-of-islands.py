class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each grid
        #   if i'ts not visited yet
        #   visit everything it's connected to
        #   island +=1
        row = len(grid)
        col = len(grid[0])

        islands = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    self.visitIsland(grid,r,c)
                    islands+=1
        return islands


    def visitIsland(self, grid: List[List[str]], r : int, c : int) :
        row = len(grid)
        col = len(grid[0])
        
        if r<0 or r>=row or c<0 or c>=col or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.visitIsland(grid, r-1,c)
        self.visitIsland(grid, r+1,c)
        self.visitIsland(grid, r,c+1)
        self.visitIsland(grid, r,c-1)