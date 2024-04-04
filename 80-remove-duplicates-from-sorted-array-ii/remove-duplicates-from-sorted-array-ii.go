func removeDuplicates(nums []int) int {
    n := len(nums)
    if n <=2 {
        return n
    }

    idx := 1
    occur := 1
    for i :=1 ; i< n ; i++ {
        if nums[i] == nums[i-1] {
            occur++
        } else {
            occur = 1
        }

        if occur <= 2{
            nums[idx] = nums[i]
            idx++
        }

    }
    return idx

}