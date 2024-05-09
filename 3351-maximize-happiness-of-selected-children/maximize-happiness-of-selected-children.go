func maximumHappinessSum(happiness []int, k int) int64 {
    sort.Slice(happiness, func(i,j int)bool{
        return happiness[i] > happiness[j]
    })
    ans := int64(0)
    turn := 0
    for i:= 0 ; i<k ; i++ {
        temp := happiness[i] - turn
        if temp < 0{
            ans += 0
        } else {
            ans += int64(temp)
        }
       turn++
    }
    return ans;
}