func isSubsequence(s string, t string) bool {
    ns := len(s)
    nt := len(t)
    if ns == 0{
        return true
    }
    sPtr := 0
    tPtr := 0

    for ; sPtr<ns && tPtr<nt; {
        // fmt.Println(string(s[sPtr]),string(t[tPtr]),sPtr,tPtr)
        if s[sPtr] != t[tPtr] {
            tPtr++
        } else{
            sPtr++
            tPtr++
        }
        if sPtr == ns{
            return true
        }
    }

    return false

}