func productExceptSelf(nums []int) []int {
    n := len(nums)
    count0 := 0 
    index0 := -1
    prod := 1
    for i:=0 ; i<n ; i++ {
        if nums[i] == 0 {
            count0++
            index0 = i
        }
        if count0 >=2 {
            break;
        }
        if nums[i]!=0 {
            prod = prod * nums[i]
        }   
    }

    if count0 == 2 {
        return make([]int,n)
    }
    if count0 == 1 {
        ans := make([]int,n)
        // fmt.Println(index0, prod)
        ans[index0] = prod
        return ans
    }

    ans := make([]int,n)
    for i:=0 ; i < n ;i++ {
        ans[i] = prod/nums[i]
    }
    return ans


}