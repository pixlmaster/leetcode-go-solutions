func getRow(rowIndex int) []int {
    var last []int
    var row []int

    for i := 0 ; i <= rowIndex ; i++ {
        row  = make([]int, i+1)
        for j := 0; j <= i ; j++ {
            if i == 0 || j == 0 || j == i {
                row[j] = 1
            } else{
                row[j] = last[j-1] + last[j]
            }
        }
        last = make([]int,i+1)
        copy(last, row)
    }
    return row
}