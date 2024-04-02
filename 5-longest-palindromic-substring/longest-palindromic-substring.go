func longestPalindrome(s string) string {
    n := len(s)
    if(n<=1){
        return s
    }
    dp := make([][]bool, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]bool, n)
    }
    start := 0
    end := 0

    for strLen := 0 ; strLen < n ;strLen++ {
        for i:=0 ; i+ strLen < n ; i++ {
            // 1 length string
            if strLen == 0 {
                dp[i][i] = true
                continue
            } 

            // start and end characters are different
            if s[i] != s[i+strLen] {
                dp[i][i+strLen] = false
                continue
            }

            // start and end characters are the same but substring does not exist
            if i+strLen-1 < i+1 {
                dp[i][i + strLen] = true
                start = i
                end = i + strLen
                continue
            }

            dp[i][i+strLen] = dp[i + 1][i+strLen - 1]
            if dp[i][i+strLen] {
                start = i
                end = i + strLen
            }

        }
    }

    return s[start:end+1]

}