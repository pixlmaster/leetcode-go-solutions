func longestCommonPrefix(strs []string) string {
    n := len(strs)

    if n  == 0 {
        return ""
    }
    if n==1 {
        return strs[0]
    }

    pref := longestCommonPrefix(strs[0:n-1])


    s1 := len(pref)
    s2 := len(strs[n-1])
    ans := ""
    for i:=0 ; i< s1 && i<s2 ; i++ {
        if strs[n-1][i] != pref[i]{
            return ans
        }
        ans += string(strs[n-1][i])
    } 
    return ans
}