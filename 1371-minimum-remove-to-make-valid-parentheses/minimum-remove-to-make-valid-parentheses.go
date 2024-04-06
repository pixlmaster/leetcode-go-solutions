func minRemoveToMakeValid(s string) string {
    n := len(s)
    // index stack
    stack := make([]int , n)
    stackPtr := 0
    set := make(map[int]bool)
    for i:=0 ; i<n ;i++ {
        // put opening brackets in stack
        if s[i] == '(' {
            stack[stackPtr] = i
            stackPtr++
        } else if s[i] == ')' {
            if stackPtr == 0 {
                set[i] = true
            } else {
                stackPtr --
            }
        }
    }
    // empty the stack
    for ; stackPtr>0 ; stackPtr-- {
        set[stack[stackPtr-1]] = true
    }
    ans := ""

    for i:=0 ; i< len(s) ; i++ {
        _, found := set[i]
        if !found {
            ans+=string(s[i])
        }
    }
    return ans
}