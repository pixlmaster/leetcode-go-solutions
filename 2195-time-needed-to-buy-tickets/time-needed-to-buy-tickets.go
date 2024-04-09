func timeRequiredToBuy(tickets []int, k int) int {
    n := len(tickets)
    time:=0
    if k != n-1 {
        time = k+1
        for i := 0 ; i<=k ; i++ {
            tickets[i]--
        }
    }

    
    for i:=0;i<n;i++ {
        if tickets[i] <= tickets[k]{
            time += tickets[i]
        } else {
            time += tickets[k]
        }
    }
    return time
}