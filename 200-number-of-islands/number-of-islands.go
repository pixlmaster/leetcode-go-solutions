func numIslands(grid [][]byte) int {
    row := len(grid)
    col := len(grid[0])

    num := 0

    for i:=0 ; i < row ; i++ {
        for j:=0 ; j< col ; j++{
            if grid[i][j] == '1' {
                dfs(grid,i,j,row, col)
                num++
            }
        }
    }
    return num
}

func dfs(grid [][]byte, i int, j int, row int, col int) {
    if i>=row || i<0 || j>=col || j<0 {
        return
    }

    // mark current visited
    grid[i][j] = '2'

    // visit top
    if i>0 && grid[i-1][j] == '1' {
        dfs(grid,i-1,j,row,col)
    }

    // visit bottom
    if i<row-1 && grid[i+1][j] == '1' {
        dfs(grid,i+1,j,row,col)
    }

    // visit left
    if j>0 && grid[i][j-1] == '1' {
        dfs(grid,i,j-1,row,col)
    }

    // visit right
    if j<col-1 && grid[i][j+1] == '1' {
        dfs(grid,i,j+1,row,col)
    }
}