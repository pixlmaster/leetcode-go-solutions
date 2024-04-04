func maxDepth(s string) int {
    n := len(s)
    max:=0;
    current :=0;
    for i :=0 ; i< n ;i++ {
        if s[i] == '(' {
            current++
            if current > max {
                max = current
            }
        } else if(s[i] == ')') {
            current--
        }
    }

    return max

}