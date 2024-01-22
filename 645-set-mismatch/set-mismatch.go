func findErrorNums(nums []int) []int {
    numLen := len(nums)
    numMap := make(map[int]bool)
    numSum := 0
    expNumSum := (numLen * (numLen + 1))/2
    numRepeat := 0

    for _, num := range nums {
        _, numFound := numMap[num]
        if numFound {
            numRepeat = num
        }
        numMap[num] = true
        numSum += num
    }

    numDiff := expNumSum - numSum
    return []int{numRepeat, numRepeat + numDiff}
}