func intToRoman(num int) string {
    ans := ""
    m := num/1000
    num = num - m*1000

    c := num/100
    num = num - c*100

    x := num/10
    num = num - x*10

    i := num/1
    num = num  - i*1

    for itr :=0 ; itr<m ; itr++ {
        ans += "M"
    }

    ans += toString(c, "M","C","D")
    ans += toString(x, "C","X","L")
    ans += toString(i, "X","I","V")
    return ans
}

func toString(num int, high string, curr string, mid string) string {
    ans := ""
    if num == 9 {
        ans += curr+ high
    } else if num>=5 {
        ans += mid
        for itr := 0 ;itr <num-5 ; itr++ {
            ans+= curr
        }
    } else if num==4{
        ans += curr + mid
    } else{
        for itr :=0 ; itr<num ; itr++ {
            ans+= curr
        }
    }
    return ans
}