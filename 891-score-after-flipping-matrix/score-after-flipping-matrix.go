func matrixScore(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    grid1 := make([][]int,m)
    for i :=0 ;i < m ; i++{
        grid1[i] = make([]int,n)
        copy(grid1[i],grid[i])
    }
    rowScore :=0
    colScore:=0
    // flip 1st columns
    for i :=0 ;i <m ; i++ {
        grid1[i][0] = grid1[i][0]^1
    }

    for i:=0 ; i< m ; i++ {
        // flip the rows
        if grid[i][0] == 0 {
            for j:=0;j<n;j++{
                grid[i][j] = grid[i][j]^1
                grid1[i][j] = grid1[i][j]^1
            }
        }
    }
    for j:=0; j < n ; j++ {
        num1 :=0
        num2 :=0
        for i:=0; i<m; i++ {
            if grid[i][j] == 1 {
                num1++
            }
            if grid1[i][j] == 1 {
                num2++
            }
        }
        if num1 >m/2 {
            rowScore+= num1*powInt(2,n-j-1)
        } else {
            rowScore+=(m-num1)*powInt(2,n-j-1)
        }

        if num2 >m/2 {
            colScore+= num2*powInt(2,n-j-1)
        } else {
            colScore+=(m-num2)*powInt(2,n-j-1)
        }
    }

    

    if rowScore> colScore {
        return rowScore
    } 
    return colScore
}

func powInt(x, y int) int {
    return int(math.Pow(float64(x), float64(y)))
}