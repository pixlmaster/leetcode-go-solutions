func maximumValueSum(nums []int, k int, edges [][]int) int64 {
    n := len(nums)
    swapped, ans, min := constructXor(nums,n,k)
    // fmt.Println(ans,min)
    if swapped %2 == 0 {
        return ans
    }
    return ans - min

}

func constructXor(nums []int, n int, k int) (int, int64 ,int64) {
    swap := 0
    ans:=int64(0)
    smallest :=int64(1000000001)
    for i:=0 ;i<n;i++ {
        xor := int64(nums[i]^k)
        if xor > int64(nums[i]) {
            ans+= xor
            swap++
            if xor - int64(nums[i]) < smallest{
                smallest = xor - int64(nums[i])
            }
        } else{
            ans+= int64(nums[i])
            if int64(nums[i]) - xor < smallest{
                smallest = int64(nums[i]) - xor
            }
        }
    }
    return swap, ans, smallest
}