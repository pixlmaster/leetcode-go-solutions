func lengthOfLastWord(s string) int {
    n := len(s)
    ans :=0
    var i int
    // ignore all whitespaces
    for i=n-1 ; i>=0 && s[i]==' ' ; i-- {

    }
    // get the len of the word
    for ; i>=0 && s[i]!=' '; i-- {
        ans++
    }
    return ans
}