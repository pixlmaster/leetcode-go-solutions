func minCostClimbingStairs(cost []int) int {
    n := len(cost)

    for cur := 2 ;cur < n ; cur ++ {
        if(cost[cur-1]<cost[cur-2]){
            cost[cur] +=  cost[cur-1]
        } else{
            cost[cur] += cost[cur-2]
        }
    }

    if cost[n-2]<cost[n-1] {
        return cost[n-2]
    } else {
        return cost[n-1]
    }
}