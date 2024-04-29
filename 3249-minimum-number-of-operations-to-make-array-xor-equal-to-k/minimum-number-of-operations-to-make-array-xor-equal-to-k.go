func minOperations(nums []int, k int) int {
    n := len(nums)
    total := k
    for i:=0 ; i< n ; i++ {
        total = total^nums[i]
    }

    flip :=0
    for ; total!=0 ; {
        if total % 2 !=0 {
            flip++
        }
        total = total/2
    }
    return flip
}