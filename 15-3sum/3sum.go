func hash(arr []int) string {
    return strconv.Itoa(arr[0]) +"," + strconv.Itoa(arr[1]) +"," + strconv.Itoa(arr[1])
}

func threeSum(nums []int) [][]int {
    n := len(nums)
    sort.Ints(nums)
    var ans [][]int
    m := make(map[string][]int)

    for idx, target := range(nums) {
        target = -target
        start := 0
        end := n-1
        for ; start < end ; {
            sum := nums[start] + nums[end]
            if sum > target || end == idx{
                end--
            } else if sum < target || start == idx{
                start++
            } else {
                // fmt.Println(nums[start],nums[end],-target)
                temp := []int{nums[start],nums[end],-target}
                sort.Ints(temp)
                m[hash(temp)] = temp
                start++
                end--
            }
        }
    }

    for _, val := range(m) {
        ans = append(ans,val)
    }

    return ans

}

