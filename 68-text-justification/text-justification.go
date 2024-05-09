func fullJustify(words []string, maxWidth int) []string {
    n:= len(words)
    count :=0
    var ans []string
    for  ;  count <n ;{
        curr :=""
        curri := 0
        remain := maxWidth
        for ; remain>0 && count < n ; {
            // required for inserting the word
            req := len(words[count])
            // if it's not the first word we need at least 1 space
            if curri >0 {
                req++
            }
            // if remaining spaces left are enough to fit the current word
            if req <= remain {
                if curri >0 {
                    curr += " "
                }
                curr += words[count]
                curri++
                count++
                remain = remain-req
            } else{
                break
            }
        }
        // fmt.Println(curr)
        // when we reach here , curr contains the string to be added with at least 1 space
        // and curri contains the number of words
        // remain contains the number of spaces to be fit
        if count < n {
            curr = normalise(curr,remain, curri)
        } else{
            for i :=0 ; i<remain ; i++ {
                curr += " "
            }
        }
        // fmt.Println(curr)
        ans = append(ans, curr)
    }
    return ans
}


func normalise(curr string, remain int, n int) string {
    // fmt.Println(curr,remain,n)
    if n == 1 {
        for i :=0 ; i<remain ; i++ {
            curr += " "
        }
        return curr
    }

    each := remain/(n-1)
    extras := (remain - each*(n-1))
    ans :=""
    for i:=0 ; i< len(curr); i++{
        if curr[i] !=' '{
            ans+=string(curr[i])
        } else{
            ans += string(curr[i])
            for i:=0 ;i<each;i++ {
                ans += " "
            }
            if extras >0 {
                ans+= " "
                extras--
            }
        }
    }
    return ans
}