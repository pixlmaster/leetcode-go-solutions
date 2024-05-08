func candy(ratings []int) int {
    n := len(ratings)
    ans := n
    for i:=1 ; i < n ;{
        if ratings[i] == ratings[i-1] {
            i++
            continue
        }

        // increasing slope
        peak :=0
        for ratings[i] > ratings[i-1] {
            peak++
            ans += peak
            i++
            if i == n {
                return ans
            }
        }

        // decreasing slope
        valley :=0
        for i<n && ratings[i] < ratings[i-1]{
            valley++;
            ans += valley
            i++
        }
        if peak< valley {
            ans -=peak
        }else{
            ans -=valley
        }
    }   
    return ans;
}