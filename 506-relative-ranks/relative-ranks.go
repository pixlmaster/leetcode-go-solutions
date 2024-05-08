
func desc(n1 int, n2 int) bool {
    return n1<=n2
}


func findRelativeRanks(score []int) []string {
    n:= len(score)
    copied := make([]int,n)
    idxMap := make(map[int]int)
    for i:=0 ; i< n ; i++ {
        copied[i] = score[i]
        idxMap[score[i]] = i
    }
    sort.Slice(copied, func(i,j int) bool{
        return copied[i]>copied[j]
    })
    // for i:=0 ; i< n ; i++ {
    //     fmt.Println(copied[i])
    // }
    ans := make([]string,n)
    for i:=0 ; i< n ; i++ {
        if i == 0 {
            ans[idxMap[copied[i]]] = "Gold Medal"
        } else if i == 1 {
            ans[idxMap[copied[i]]] = "Silver Medal"
        } else if i == 2 {
            ans[idxMap[copied[i]]] = "Bronze Medal"
        } else {
            ans[idxMap[copied[i]]] = strconv.Itoa(i+1)
        }
    }
    return ans
}