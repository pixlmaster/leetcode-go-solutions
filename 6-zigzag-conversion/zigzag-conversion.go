func convert(s string, numRows int) string {
    if numRows==1 {
        return s
    }
    n := len(s)
    pat := make([]string,numRows)
    ans := ""
    for i:=0 ; i < n ; i++ {    
        row := i%(2*numRows-2)
        if row >= numRows {
            row = numRows -2 - (row-numRows)
        }
        pat[row] += string(s[i])
    }

    for i:=0;i<numRows;i++ {
        ans +=pat[i]
    }
    return ans
}