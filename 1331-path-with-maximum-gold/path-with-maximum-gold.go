func getMaximumGold(grid [][]int) int {
    max := -1
    m := len(grid)
    n := len(grid[0])
    for i:=0 ; i< m ; i++ {
        for j :=0 ; j<n ; j++{
            visited := make([][]bool,m)
            for i:=0 ; i< m ; i++ {
                visited[i] = make([]bool,n)
            }
            curr := dfs(grid, i,j,m,n,visited)
            if curr > max {
                max = curr
            }
        }
    }
    return max
}


func dfs(grid [][]int,i int,j int, m int, n int, visited [][]bool) int{
    if i<0 || j<0 || i >=m || j >= n || visited[i][j] || grid[i][j]==0{
        return 0
    }
    // fmt.Println(i,j)
    visited[i][j] = true
    left := dfs(grid,i,j-1,m,n,visited)
    right := dfs(grid,i,j+1,m,n,visited)
    top:= dfs(grid,i-1,j,m,n,visited)
    bot := dfs(grid,i+1,j,m,n,visited)
    maxRow := maxInt(left,right)
    maxCol := maxInt(top,bot)
    max := maxInt(maxRow,maxCol)
    visited[i][j] = false
    return max + grid[i][j]

}

func maxInt(a,b int) int {
    if a>b {
        return a
    }
    return b
}