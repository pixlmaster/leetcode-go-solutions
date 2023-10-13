func minCostClimbingStairs(cost []int) int {
    // minCost[i] = min(minCost[i-1]+cost[i-1],minCost[i-2] + cost[i-1])
    n := len(cost)
    var minCost [10001]int

    for cur := 0 ;cur < n+1 ; cur ++ {
        if(cur==0 || cur == 1){
            minCost[cur] = 0
        } else {
            cost1 := minCost[cur-1] + cost[cur-1]
            cost2 := minCost[cur-2] + cost[cur-2]
            if(cost1<cost2){
                minCost[cur] =  cost1
            } else{
                minCost[cur] = cost2
            }
            
        }
    }

    return minCost[n]
}