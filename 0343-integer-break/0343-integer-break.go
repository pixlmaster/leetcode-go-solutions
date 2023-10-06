func integerBreak(n int) int {

    if n ==2 {
        return 1
    } else if n ==3 {
        return 2
    }

    maxProd := 1
    k := n / 3
    rem := n % 3

    for i := 0 ; i < k-1 ; i++ {
        maxProd = maxProd * 3
    }

    if rem ==0 {
        return maxProd * 3
    } else if rem ==1 {
        return maxProd * 4
    } else {
        return maxProd * 6
    }

}