

func numWays(steps int, n int) int {
	mod := 1000000000 + 7
	if steps < n {
		n = steps
	}
	var dp = make([][]int, n)
	for i:=0 ; i< n ; i++{
		dp[i] = make([]int,steps + 1)
	}

	dp[0][0] = 1

	for j := 1 ; j <= steps ; j ++ {
		for i:=0; i < n ; i++ {
			dp[i][j] = dp[i][j-1]
			if(i>0){
				dp[i][j]+=dp[i-1][j-1]
			}
			if(i<n-1){
				dp[i][j] += dp[i+1][j-1]
			}


			dp[i][j] = dp[i][j]%mod
			
		}
	}

	return dp[0][steps]

}