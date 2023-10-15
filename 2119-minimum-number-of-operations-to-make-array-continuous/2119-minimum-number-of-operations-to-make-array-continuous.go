func minOperations(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    numset := make([]int,n)
    unique :=0

    for i:= 0 ; i<n;i++{
        if i>0 && nums[i]==nums[i-1]{
            continue
        }
        numset[unique]=nums[i]
        unique++
    }

    min:=n

    j := 0
    for i:= 0 ; i < unique; i++{
        r := numset[i] + n - 1 
        for ; j < unique && numset[j] <= r ; j++ {
        } 
        if (n-(j-i)<min){
            min = n-(j-i)
        }

    }   

    return min

}
