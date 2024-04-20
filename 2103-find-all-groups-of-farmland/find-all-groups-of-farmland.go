func findFarmland(land [][]int) [][]int {
    m := len(land)
    n := len(land[0])
    var ans [][]int


    for i :=0 ; i< m ; i++ {
        for j :=0 ; j<n ; j ++ {
            if land[i][j] == 1 {
                // do traversal
                sub := make([]int,4)
                sub[0] = i
                sub[1] = j
                starti := i
                startj := j

                for ; starti<m && land[starti][j] == 1 ; starti++{
                }
                for ; startj<n && land[i][startj] == 1 ; startj++{
                }
                sub[2] = starti -1
                sub[3] = startj -1

                for itri := i ; itri < starti ; itri++{
                    for itrj := j ; itrj < startj ; itrj++ {
                        land[itri][itrj] = 0
                    }
                }
                j = startj
                ans = append(ans,sub)
            }
        }
    }
    return ans

}