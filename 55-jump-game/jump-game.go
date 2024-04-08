
func canJump(nums []int) bool {
    can := make(map[int]int)
    can[0] = 1
    if recurse(nums,len(nums)-1,can) >0 {
        return true
    } else{
        return false
    }
}


func recurse(nums []int, idx int, can map[int]int) int{
    // base cases
    if idx <= 0 {
        return 1
    }
    // fmt.Println(idx, can[idx])
    if can[idx] != 0 {
        return can[idx]
    }
    for i:= idx-1 ; i >=0 ; i-- {
        if nums[i] -  (idx - i)>=0 {
            if recurse(nums,i,can) ==1 {
                can[idx] = 1
                // fmt.Println(idx,true)
                return 1
            }
        }
    }
    // fmt.Println(idx,false)
    can[idx] = -1
    return -1

}