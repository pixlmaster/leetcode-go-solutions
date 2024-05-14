func maxPointsInsideSquare(points [][]int, s string) int {
    n := len(points)
    square := make([][]int ,n)
    for i:=0 ; i< n ; i++ {
        square[i] = make([]int,2)
        square[i][0] = maxAbs(points[i][0], points[i][1])
        square[i][1] = toInt(s[i])
    }

    sort.Slice(square, func(i,j int) bool{
        return square[i][0] < square[j][0]
    }) 

    set := make(map[int]bool)
    for i:=0; i <n ; {
        currentSet := make(map[int]bool)
        sq := square[i][0]
        for ; i<n && square[i][0] == sq ; i++ {
            // fmt.Println(square[i][0], square[i][1])
            _, exists := set[square[i][1]]
            _, exists1 :=currentSet[square[i][1]]
            if exists || exists1 {
                return len(set)
            }
            currentSet[square[i][1]] = true
        }
        for key, _ := range(currentSet) {
            set[key] = true
        } 
    }

    return len(set)

}

func maxAbs(a,b int) int {
    if abs(a) < abs(b) {
        return abs(b)
    }
    return abs(a)
}

func abs(a int) int {
    if a<0 {
        return -a
    }
    return a
}

func toInt(b byte) int{
    return int(b)-'a'
}