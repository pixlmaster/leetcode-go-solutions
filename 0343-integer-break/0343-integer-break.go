func integerBreak(n int) int {
    maxProd := 1
    for k := 2 ; k <= n ; k++ {
        currMaxProd := 1
        div := n / k
        rem := n % k
        for i := 0 ; i<k ; i ++ {
            if rem > 0 {
                currMaxProd = currMaxProd*(div+1)
                rem--
            } else {
                currMaxProd = currMaxProd*(div)
            }
            
        }
        if currMaxProd > maxProd {
            maxProd = currMaxProd
        }
    }

    return maxProd
 
}