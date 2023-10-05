func majorityElement(nums []int) []int {
    // candidate elements
    cand1 := 0
    cand2 := 0
    // freq of candidate elements
    freq1 := 0
    freq2 := 0

    // get the candidates
    for i := 0 ; i < len(nums) ; i++ {
        if freq1 == 0 && nums[i] != cand2 {
            freq1++
            cand1 = nums[i]
        } else if freq2 == 0 && nums[i] != cand1 {
            freq2++
            cand2 = nums[i]
        } else if nums[i] == cand1 {
            freq1++
        } else if nums[i] == cand2 {
            freq2++
        } else {
            freq1--
            freq2--
        }
    }

    freq1 = 0
    freq2 = 0
    // second pass to confirm
    for i := 0 ; i < len(nums) ; i++ {
        if nums[i] == cand1 {
            freq1++
        } else if nums[i] == cand2 {
            freq2++
        }
    }

    var ans []int
    if freq1 > (len(nums)/3) {
        ans = append(ans, cand1)
    }
    if freq2 > (len(nums)/3) {
        ans = append(ans, cand2)
    }

    return ans


}