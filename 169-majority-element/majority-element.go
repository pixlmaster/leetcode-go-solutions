func majorityElement(nums []int) int {
    vote := 0 
    currentElem := nums[0]

    for i := 0 ; i < len(nums) ; i++ {
        if nums[i] == currentElem {
            vote++
        } else{
            vote--
            if vote == 0 {
                currentElem = nums[i]
                vote++
            }
        }
    }
    return currentElem

}