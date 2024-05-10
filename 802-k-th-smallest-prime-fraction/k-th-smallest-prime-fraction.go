type fraction struct{
    fract float32
    i int
    j int
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
    n := len(arr)
    m := (n*(n-1))/2
    fact := make([]fraction ,m)
    count :=0
    for i:= 0 ;i < n ; i++ {
        for j := i+1 ; j< n ; j++ {
            fact[count] = fraction{float32(arr[i])/float32(arr[j]),i,j}
            count++
        }
    }

    sort.Slice(fact, func(i, j int) bool{
        return fact[i].fract < fact[j].fract
    })

    // for i:= 0 ;i < m ; i++ {
    //     fmt.Println(fact[i])
    // }

    return []int{arr[fact[k-1].i], arr[fact[k-1].j]}

}