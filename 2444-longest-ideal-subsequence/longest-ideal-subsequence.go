import "fmt"
func longestIdealString(s string, k int) int {
    n := len(s)
    dp := make([]int,26)

    global := 1
    for i :=0 ; i < n ; i++ {
        curr := int(s[i]) - int('a') 
        start := curr - k
        if start <0 {
            start =0
        }
        end := curr +k 
        if end > 25 {
            end = 25
        }
        max :=1
        // fmt.Println(curr , start, end)
        for j:= start ; j <=end ; j++{
            if dp[j] + 1 > max {
                max = dp[j]+1
            }
        }
        dp[curr] = max
        if max > global{
            global = max
        }
        // for itr :=0 ;itr < 26 ;itr++ {
        //     if dp[itr] != 0 {
        //         fmt.Printf("%s , %d ",string('a'+itr), dp[itr])
        //     }
        // }
        // fmt.Println()
    }


    return global

}
