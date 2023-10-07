func numOfArrays(n int, m int, k int) int {
    var ways [51][51][101]int
    var MOD int
    MOD = 1e9 + 7;

    // base case
    for max :=0 ;max <=m ;max++ {
        ways[n][0][max] = 1
    }

    //elements placed till now
    for i := n-1 ; i >= 0 ; i-- {
        for maxYet := m ; maxYet >=0 ; maxYet-- {
            // iterate for all possible max possible element yet
            for rem := 0 ; rem <= k ; rem++ {
                ans := 0
                for itr := 1 ; itr <= maxYet ; itr ++ {
                    ans += ways[i+1][rem][maxYet]
                    ans = ans % MOD
                }

                if rem > 0 {
                    for itr := maxYet+1  ; itr <= m ; itr ++ {
                        ans += ways[i+1][rem-1][itr] 
                        ans = ans % MOD
                    }
                }
                ways[i][rem][maxYet] = ans

            }
        }
    }

    return ways[0][k][0]



} 