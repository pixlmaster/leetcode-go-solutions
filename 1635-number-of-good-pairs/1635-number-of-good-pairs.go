func numIdenticalPairs(nums []int) int {
    var freq [101]int

    for idx := 0 ; idx < len(nums) ; idx ++ {
        freq[nums[idx]]++
    }

    numPairs := 0
    for idx := 0 ; idx < 101 ; idx ++ {
        if freq[idx] > 1 {
            numPairs += ((freq[idx]-1) * (freq[idx]))/2
        }
    }

    return numPairs

}