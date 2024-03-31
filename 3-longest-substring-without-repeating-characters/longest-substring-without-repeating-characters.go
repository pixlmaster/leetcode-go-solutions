func lengthOfLongestSubstring(s string) int {
    start := 0
    end := 0
    maxLen := 0 
    strLen := len(s)
    strSet := make(map[byte]bool)
    if strLen == 0 || strLen == 1 {
        return strLen
    }

    for ; end < strLen ; end++ {
        strChar := s[end]
        isPresent, isFound := strSet[strChar]
        if !isFound || !isPresent {
            if end - start + 1 > maxLen {
                maxLen = end - start +1
            }
            strSet[strChar] = true
            continue
        }
        // already exists
        for ; s[start] != strChar ; start++ {
            strSet[s[start]] = false
        }
        start++

    }
    return maxLen

}