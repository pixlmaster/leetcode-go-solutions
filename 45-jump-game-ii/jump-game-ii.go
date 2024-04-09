
func jump(nums []int) int {
    can := make(map[int]int)
    can[0] = 0
    return recurse(nums,len(nums)-1,can)
}


func recurse(nums []int, idx int, can map[int]int) int{
    // base cases
    if idx <= 0 {
        return 0
    }
    // fmt.Println(idx, can[idx])
    if can[idx] != 0 {
        return can[idx]
    }
    min := 100000
    for i:= idx-1 ; i >=0 ; i-- {
        if nums[i] -  (idx - i)>=0 {
            steps := recurse(nums,i,can)
            if steps +1 < min {
                min = steps + 1
            }
        }
    }
    // fmt.Println(idx,false)
    can[idx] = min
    return min

}