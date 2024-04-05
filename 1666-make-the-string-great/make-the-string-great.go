func makeGood(s string) string {
    var diff byte
    diff = 'a' - 'A'
    prevlength := -1
    for ; prevlength != len(s) ;{
        prevlength = len(s)
        for i := 0 ; i < len(s) - 1 ; i++ {
            currentDiff := s[i+1] - s[i]
            if currentDiff == diff || currentDiff + diff == 0 {
                s = s[0:i] + s[i+2:len(s)]
            }
        }
    }
    return s
}