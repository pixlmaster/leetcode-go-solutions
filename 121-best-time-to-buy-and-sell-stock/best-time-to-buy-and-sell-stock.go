func maxProfit(prices []int) int {
    profit :=0 
    min := prices[0]
    n := len(prices)
    for i:=0 ;i<n ;i++{
        if prices[i] - min > profit {
            profit = prices[i] - min
        }
        if prices[i]<min {
            min = prices[i]
        }
    }
    return profit
}