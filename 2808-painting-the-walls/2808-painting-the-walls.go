
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}

func paintWalls(cost []int, time []int) int {
	n := len(cost)

	var dp [501][501]int

	for i := 1; i <= n; i++ {
    dp[n][i] = 1e9;
  }

	for i :=n-1 ;i >= 0 ; i--  {
		for  remain := 1; remain <= n ; remain++ {
			paint := cost[i] + dp[i+1][max(0, remain - time[i]-1 )]
			dontPaint := dp[i+1][remain]
			dp[i][remain] = min(paint,dontPaint)
		

		} 
	}

	return dp[0][n]

}