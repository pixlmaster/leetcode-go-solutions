func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int)
    for index, value := range nums {
        compIndex, exists := hmap[target - value]
        if exists {
            return []int{index, compIndex}
        }
        hmap[value] = index
    }
    return []int{}
}