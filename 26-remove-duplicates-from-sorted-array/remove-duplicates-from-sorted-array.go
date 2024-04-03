func removeDuplicates(nums []int) int {
    n := len(nums)
    if n <=1 {
        return n
    }
    slowPtr := 0 
    fastPtr := 0

    k := 1
    for ; fastPtr <n ; fastPtr ++ {
        if nums[fastPtr] != nums[slowPtr] {
            slowPtr++
            nums[slowPtr] = nums[fastPtr]
            k++
        }
    }
    return k
}