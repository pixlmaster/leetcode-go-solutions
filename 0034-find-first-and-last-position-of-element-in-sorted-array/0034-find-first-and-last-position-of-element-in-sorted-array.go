func findl(nums *[]int, l int, r int, target int) int {
    // base cases
    if l > r || l < 0 || r >= len(*nums){
        return -1
    }
    mid := (l + r)/2

    // found
    if (*nums)[mid] == target{
        // mid is the answer
        if mid == 0 || (*nums)[mid-1] != target {
            return mid
        } else {
            // search left
            return findl(nums, l, mid-1, target )
        }
    } else if (*nums)[mid] < target{
        // seach right
        return findl(nums, mid+1, r, target)
    } else {
        // search left
        return findl(nums, l, mid-1, target)
    }

}

func findr(nums *[]int, l int, r int, target int) int {
    // base cases
    if l > r || l < 0 || r >= len(*nums){
        return -1
    }
    mid := (l + r)/2

    // found
    if (*nums)[mid] == target{
        // mid is the answer
        if mid == len(*nums)-1 || (*nums)[mid+1] != target {
            return mid
        } else {
            // search right
            return findr(nums, mid+1, r, target )
        }
    } else if (*nums)[mid] < target{
        // seach right
        return findr(nums, mid+1, r, target)
    } else {
        // search left
        return findr(nums, l, mid-1, target)
    }

}


func searchRange(nums []int, target int) []int {
    var ans []int
    ans = append(ans, findl(&nums,0,len(nums)-1,target))
    ans = append(ans, findr(&nums,0,len(nums)-1,target))
    return ans
}