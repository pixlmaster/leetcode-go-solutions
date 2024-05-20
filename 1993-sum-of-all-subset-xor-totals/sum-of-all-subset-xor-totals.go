func subsetXORSum(nums []int) int {
    n:=len(nums)
    ans:=0
    num := pow(2,n)
    for bits:=0;bits<num ; bits++ {
        temp := bits
        curr :=0
        itr := n-1
        for ; temp!=0 ; {
            if temp%2==1 {
                curr ^=nums[itr]
            }
            temp = temp >> 1
            itr--
        }
        ans += curr
    }
    return ans
}

func pow(a,b int) int {
    return int(math.Pow(float64(a), float64(b)))
}