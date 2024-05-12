func largestLocal(grid [][]int) [][]int {
    n := len(grid)
    ans := make([][]int,n-2)
    for i:=0;i<n-2;i++{
        for j:=0 ; j< n-2; j++ {
            m:=-1
            for i1 := i ; i1 < i+3 ; i1++ {
                for j1 := j ; j1<j+3 ; j1++ {
                    m = max(m,grid[i1][j1])
                }
            }
            ans[i] = append(ans[i], m)
        }
    }
    return ans

}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}