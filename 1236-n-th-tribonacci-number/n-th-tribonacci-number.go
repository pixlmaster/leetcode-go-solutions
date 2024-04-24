func tribonacci(n int) int {
    dp := make([]int, n+1)
    if n== 0 {
        return 0
    }
    if n==1 || n==2 {
        return 1
    }
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    return recurse(n, dp)
}

func recurse(n int, dp []int) int {
    if n==0 {
        return 0
    }
    if dp[n]!=0 {
        return dp[n]
    }

    dp[n] =  recurse(n-1,dp) + recurse(n-2,dp) + recurse(n-3,dp)
    return dp[n]
}