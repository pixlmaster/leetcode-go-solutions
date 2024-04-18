func islandPerimeter(grid [][]int) int {
    row := len(grid)
    col := len(grid[0])

    visited := make([][]bool ,row)
    for i :=0 ; i<row ;i++ {
        visited[i] = make([]bool,col)
    }


    for i:= 0 ; i< row ; i++ {
        for j:=0 ; j< col; j++ {
            if grid[i][j] == 1 {
                return perimeter(grid,i,j,visited, row, col)
            }
        }
    }
    return 0

}


func perimeter(grid [][]int,i int,j int,visited [][]bool, row int, col int) int{
    // out of bounds base case
    if i<0 || i>=row || j < 0 || j >=col {
        return 0
    }
    ans := 0
    var top,bot,left,right int
    if i == 0 {
        top = 0
    } else {
        top = grid[i-1][j]
    }
    if j == 0 {
        left = 0
    } else{
        left = grid[i][j-1]
    }
    if i == row-1 {
        bot = 0
    } else {
        bot = grid[i+1][j]
    }

    if j == col-1 {
        right = 0
    } else {
        right = grid[i][j+1]
    }

    visited[i][j] = true


    if top == 1 && !visited[i-1][j] {
        ans += perimeter(grid,i-1,j,visited,row,col)
    } else if top ==0 {
        ans+=1
    }

    if bot == 1 && !visited[i+1][j] {
        ans += perimeter(grid,i+1,j,visited,row,col)
    } else if bot ==0{
        ans+=1
    }

    if left == 1 && !visited[i][j-1] {
        ans += perimeter(grid,i,j-1,visited,row,col)
    } else if left ==0 {
        ans+=1
    }

    if right == 1 && !visited[i][j+1] {
        ans += perimeter(grid,i,j+1,visited,row,col)
    } else if right ==0 {
        ans+=1
    }

    // fmt.Println(i,j,ans)

    return ans

}