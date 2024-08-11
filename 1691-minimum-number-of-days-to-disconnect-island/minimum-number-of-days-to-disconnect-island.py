class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        """
        count number of islands , if already 2 > return 0
        else:
            classify tiles according to number of sides it is sorrounded by water
            4:
            3:
            2:
            1:
            if there is a 4 tile, then that's the only island piece make it 0 -> return 1
            if there a 3 tile, make the land side of it as 0 and check, return 1
            if there a 2 tile, make the the 2 land side of it is and water and check
            if there are 1 tile, makt the other 3 land side of it and water and check
            if still no unique case make everything water
        """

        numIslands = self.countIslands(grid)
        if numIslands != 1:
            return 0

        tileClassification = {
            4: [],
            3: [],
            2: [],
            1: [],
            0: []
        }
        self.classifyIslands(grid, tileClassification)
        # print(tileClassification)
        if len(tileClassification[4]) > 0:
            return 1
        if len(tileClassification[3]) > 0:
            for tup in tileClassification[3]:
                if self.delAndCheck(grid, tup[0], tup[1]):
                    return 1
        if len(tileClassification[2]) > 0:
            for tup in tileClassification[2]:
                if self.delAndCheck(grid, tup[0], tup[1]):
                    if self.checkForEdgeCase(grid):
                        return 1
                    return 2
        # edge cases
        return len(tileClassification[4] + tileClassification[3] + tileClassification[2] + tileClassification[1] +
                   tileClassification[0])

    def checkForEdgeCase(self, grid: list[list[int]]):
        row = len(grid)
        col = len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if self.countIslands(grid) !=1:
                    grid[r][c] = 1
                    return True
                grid[r][c] = 1
        
        return False

    def delAndCheck(self, grid: list[list[int]], r: int, c: int) -> bool:
        # delete all surrounding land from this tile
        row = len(grid)
        col = len(grid[0])
        top = False
        bottom = False
        left = False
        right = False
        ans = False

        # check top
        if r > 0 and grid[r - 1][c] == 1:
            grid[r - 1][c] = 0
            top = True
        #check bottom
        if r < row - 1 and grid[r + 1][c] == 1:
            grid[r + 1][c] = 0
            bottom = True

        # check right
        if c < col - 1 and grid[r][c + 1] == 1:
            grid[r][c + 1] = 0
            right = True

        # check left
        if c > 0 and grid[r][c - 1] == 1:
            grid[r][c - 1] = 0
            left = True
        if self.countIslands(grid) != 1:
            ans = True

        if top:
            grid[r - 1][c] = 1
        if bottom:
            grid[r + 1][c] = 1
        if left:
            grid[r][c - 1] = 1
        if right:
            grid[r][c + 1] = 1

        return ans

    def classifyIslands(self, grid: list[list[int]], tileClassification: dict[int, list[(int, int)]]):
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 1:
                    continue
                water = 0
                # check top
                if r == 0 or grid[r - 1][c] == 0:
                    water += 1
                #check bottom
                if r == row - 1 or grid[r + 1][c] == 0:
                    water += 1

                # check right
                if c == col - 1 or grid[r][c + 1] == 0:
                    water += 1

                # check left
                if c == 0 or grid[r][c - 1] == 0:
                    water += 1

                tileClassification[water].append((r, c))

    def countIslands(self, grid: list[list[int]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    self.dfs(grid, r, c, visited)
                    ans += 1

        return ans

    def dfs(self, grid: list[list[int]], r: int, c: int, visited: set[(int, int)]):
        visited.add((r, c))
        row = len(grid)
        col = len(grid[0])

        # visit left
        if c > 0 and (r, c - 1) not in visited and grid[r][c - 1] == 1:
            self.dfs(grid, r, c - 1, visited)

        # visit right
        if c < col - 1 and (r, c + 1) not in visited and grid[r][c + 1] == 1:
            self.dfs(grid, r, c + 1, visited)

        # visit top
        if r > 0 and (r - 1, c) not in visited and grid[r - 1][c] == 1:
            self.dfs(grid, r - 1, c, visited)

        # visit bottom
        if r < row - 1 and (r + 1, c) not in visited and grid[r + 1][c] == 1:
            self.dfs(grid, r + 1, c, visited)


"""
[[1,1,1,1,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,1,1],
[1,1,1,1,1,0,1,1,1]]

[[1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 0, 1]]


[[1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 0, 1]]

"""
