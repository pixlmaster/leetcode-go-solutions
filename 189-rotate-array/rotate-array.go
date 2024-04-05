func rotate(nums []int, k int)  {
    n := len(nums)
    if n <=1 {
        return
    }
    k = k%n
    if k==0{
        return
    }
    reverse(nums,n-k,0)
    reverse(nums, k, n-k)
    reverse(nums,n,0)
}

func reverse(nums []int , numLen int, start int){
    for i:=start ; i<= start + ((numLen -1)/2) ; i++ {
        temp := nums[i]
        nums[i] = nums[start + start + numLen-i-1]
        nums[start + start + numLen-i-1] = temp
    }
}