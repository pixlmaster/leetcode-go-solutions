func canCompleteCircuit(gas []int, cost []int) int {
    n := len(gas)
    current:=0
    start:=0
    deficit := 0
    currentDef :=0
    for i:=0 ; i< n ; i++ {
        current += gas[i] - cost[i]
        deficit += gas[i] - cost[i]
        // fmt.Println(current)
        // if you cannot reach the next station, start at the next station
        if current < 0 {
            start = i+1
            currentDef=deficit
            // fmt.Println(current, deficit, start)
            current = 0
        }
    }
    if start >=n {
        return -1
    }
    // fmt.Println(start,current, currentDef)
    if current + currentDef >=0 {
        return start
    }
    return -1

}