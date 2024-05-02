func findMaxK(nums []int) int {
    n := len(nums)
    hash := make(map[int]bool)
    for i:=0 ; i < n ; i++{
        hash[nums[i]] = true
    }
    largest := -1
    for i:=0 ; i < n ; i++{
        if nums[i] > 0{
             _, exists := hash[-nums[i]]
             if exists {
                if nums[i] > largest {
                    largest = nums[i]
                }
             }
        }
    }
    return largest
}