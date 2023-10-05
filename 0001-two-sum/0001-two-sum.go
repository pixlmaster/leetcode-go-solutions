func twoSum(nums []int, target int) []int {
    sumMap := make(map[int]int)

    for idx ,curr := range nums {
        toFind := target - curr
        if toFindIdx, ok := sumMap[toFind];ok {
            return []int{idx,toFindIdx}
        }
        sumMap[curr] = idx
        
    }
    return nil;
}