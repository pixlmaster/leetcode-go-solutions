func equalSubstring(s string, t string, maxCost int) int {
    n := len(s)
    cost := make([]int,n)
    for i :=0 ; i< n ; i++ {
        cost[i] = abs(int(s[i]) - int(t[i]))
    }
    ans := 0 
    for i :=0 ; i< n ; {
        curr :=0
        j:=i
        for ; j < n ;  {
            curr += cost[j]
            if curr > maxCost {
                break
            }
            if (j-i +1) > ans {
                ans = (j-i + 1)
            }
            j+=1
        }
        if j== n {
            break
        }
        incr := true
        for ;curr > maxCost ; {
            curr -= cost[i]
            i+=1
            incr = false
        }
        if incr {
            i++
        }
    }
    return ans
}


func abs(a int) int {
    if a<0 {
        return -a
    }
    return a
}
