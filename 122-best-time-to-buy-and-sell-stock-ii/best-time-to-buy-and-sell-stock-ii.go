func maxProfit(prices []int) int {
    n := len(prices)
    if n <=1 {
        return 0
    }
    profit :=0
    for i:= 0 ; i < n ; i++ {
                fmt.Println(i) 

        // search for the smallest
        smallest := 100000
        for ; i < n-1 && prices[i+1] < prices[i]; i++{
        }
        // fmt.Println(i) 
        if i == n-1{
            continue
        }
        smallest = prices[i]
        // search for the largest
        largest :=-1
        for ; i < n-1 && prices[i] < prices[i+1]; i++{
        }
                // fmt.Println(i) 

        if(i==n-1){
            largest = prices[n-1]
        } else{
            largest = prices[i]
        }
        // fmt.Println(smallest,largest)
        profit += largest - smallest
    }

    return profit
}