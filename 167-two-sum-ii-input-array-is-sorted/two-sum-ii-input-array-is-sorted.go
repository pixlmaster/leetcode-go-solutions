func twoSum(numbers []int, target int) []int {
    n := len(numbers)
    ptr1 := 0
    ptr2 := n-1
    for ; ptr1<ptr2 ; {
        sum := numbers[ptr1] + numbers[ptr2] 
        if sum > target {
            ptr2--
        } else if sum <target {
            ptr1++
        } else {
            return []int{ptr1+1,ptr2+1}
        }
    }
    return []int{}
}