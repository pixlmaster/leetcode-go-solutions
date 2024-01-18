func uniqueOccurrences(arr []int) bool {
    // freqMap stores the frequency of elements in arr
    freqMap := make(map[int]int)
    for _ , arrElem := range arr {
        _, isArrElemPresent := freqMap[arrElem] 
        if isArrElemPresent {
            // if element is present
            freqMap[arrElem]++
        } else{
            freqMap[arrElem] = 1
        }
    }

    // stores the set of frequencies present
    freqSet := make(map[int]bool)

    for _, freq := range freqMap {
        _, isFreqPresent := freqSet[freq]
        if isFreqPresent {
            return false
        }
        freqSet[freq] = true
    }
    return true

}