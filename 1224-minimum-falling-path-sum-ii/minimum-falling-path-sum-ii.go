type point struct {
    val int
    idx int
}

type minrow struct {
    min1 int
    idx1 int
    min2 int
    idx2 int
}

func minFallingPathSum(grid [][]int) int {
    n := len(grid)
    if n == 1 {
        return grid[0][0]
    }
    if n == 2 {
        if grid[0][0] + grid[1][1] < grid[0][1] + grid[1][0]{
            return grid[0][0] + grid[1][1]
        } else{
            return grid[0][1] + grid[1][0]
        }
    }


    small3 := make([][]point,n)
    for i:=0 ;i <n ; i++ {
        small3[i] = make([]point,3)
    }

    // populate small3
    for i :=0 ; i< 1 ; i++ {
        // smallest
        small3[i][0] = point{100,-1}
        small3[i][1] = point{100,-1}
        small3[i][2] = point{100,-1}
        for j :=0 ; j< n ; j++ {
            if grid[i][j] < small3[i][0].val {
                small3[i][0].val = grid[i][j]
                small3[i][0].idx = j
            }
        }
        // 2nd smallest
        for j :=0 ; j< n ; j++ {
            if j == small3[i][0].idx {
                continue;
            }
            if grid[i][j] < small3[i][1].val {
                small3[i][1].val = grid[i][j]
                small3[i][1].idx = j
            }
        }
        // 3rd smallest
        for j :=0 ; j< n ; j++ {
            if j == small3[i][0].idx || j == small3[i][1].idx {
                continue;
            }
            if grid[i][j] < small3[i][2].val {
                small3[i][2].val = grid[i][j]
                small3[i][2].idx = j
            }
        }

    }


    dp := make([][]int,n)
    for i :=0 ;i< n ; i++ {
        dp[i] = make([]int,n)
    }
    prev1 := small3[0][0].idx                

    prev2 := small3[0][1].idx

    for i:=0 ; i< n ; i ++ {
        new1 := 100000
        new1i := -1
        new2 := 100000
        new2i := -1
        for j:=0 ; j <n ;j ++ {
            if i == 0 {
                dp[0][j] = grid[i][j]
                new1i = prev1
                new2i = prev2
                continue
            }
            if j == prev1 {
                dp[i][j] = dp[i-1][prev2] + grid[i][j]
            } else {
                dp[i][j] = dp[i-1][prev1] + grid[i][j]
            }
            if dp[i][j] < new1 {
                new1 = dp[i][j]
                new1i = j
            }

        }
        for j := 0 ; j< n ;j ++ {
            if dp[i][j] < new2 && j!=new1i {
                new2 = dp[i][j]
                new2i = j
            } 
        }
        // fmt.Println(i,new1i, new2i)

        prev1 = new1i
        prev2 = new2i

        // fmt.Println()
    }

    return min(dp[n-1][prev1],dp[n-1][prev2])


}

func min (n1 int, n2 int) int {
    if n1 < n2 {
        return n1
    }
    return n2
}