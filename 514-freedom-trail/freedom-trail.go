func findRotateSteps(ring string, key string) int {
    ringLen := len(ring)
    ptr:=0
    keyPtr :=0

    idxHash := make([][]int,26)
    mem := make([][]int, ringLen)

    // hash the key vales
    for i:=0 ; i < ringLen ; i++ {
        mem[i] = make([]int,len(key))
        idx := int(ring[i]) - int('a')
        idxHash[idx] = append(idxHash[idx],i)
    }

    return dfs(ring,key,ptr,keyPtr,idxHash,mem)
}


func dfs(ring string, key string, ptr int, keyPtr int,idxHash [][]int, mem [][]int) int{
    if keyPtr >= len(key) || ptr >= len(ring){
        return 0
    }
    keyChar := int(key[keyPtr]) - int('a')
    ringChar := int(ring[ptr]) - int('a')
    if keyChar == ringChar {
        return 1 + dfs(ring,key,ptr,keyPtr+1,idxHash,mem)
    }

    if mem[ptr][keyPtr] >0 {
        return mem[ptr][keyPtr]
    }

    smallest :=1000000
    for _, index := range(idxHash[keyChar]) {
        // fmt.Println("moving from ", ptr," to ", index)
        // move to the index
        steps :=  dist(index,ptr,len(ring))
        // fmt.Println("steps taken ", steps)
        // press it
        steps += 1
        // next step
        steps += dfs(ring,key,index,keyPtr+1,idxHash,mem)
        if steps < smallest {
            smallest = steps
        }
    }
    mem[ptr][keyPtr] = smallest
    return smallest

}

func dist(idx1 int, idx2 int, size int) int{
    dist1 := abs(idx1 - idx2) 
    dist2 := abs(size - dist1)
    if dist1 < dist2 {
        return dist1
    }
    return dist2
}

func abs(n int) int{
    if n<0 {
        return -n
    }
    return n
}