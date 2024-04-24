type RandomizedSet struct {
    // hmap stores the value fo the element and the correspodning index in the list
    hmap map[int]int
    imap map[int]int
    random []int
}


func Constructor() RandomizedSet {
    return RandomizedSet{make(map[int]int), make(map[int]int), make([]int,0)}
}


func (this *RandomizedSet) Insert(val int) bool {
    _, exists := this.hmap[val]
    if exists {
        return false
    }
    this.hmap[val] = len(this.random)
    this.imap[len(this.random)] = val
    this.random = append(this.random, val)
    return true
}

func (this *RandomizedSet) printarr() {
    for i:=0 ; i< len(this.random) ; i++ {
        fmt.Println(this.random[i])
    }
}

func (this *RandomizedSet) Remove(val int) bool {
    index, exists := this.hmap[val]
    // fmt.Println("deletion" , val, exists)
    // this.printarr()
    if exists {
        delete(this.hmap,val)
        // swapped last element with the current element and reduce size by 1
        this.random[index] = this.random[len(this.random)-1]
        this.random = this.random[:len(this.random)-1]
        // fmt.Println("post deletion ", index)
        // this.printarr()
        if len(this.random) > 0 && index < len(this.random){
            // swapped element is now at the index
            swappedVal := this.random[index]
            // update swappedElem values
            this.imap[index] = swappedVal
            this.hmap[swappedVal] = index
        }
        delete(this.imap, len(this.random))
        return true
    }
    return false
}

func (this *RandomizedSet) GetRandom() int {
    if len(this.random) == 1{
        return this.random[0]
    }
    r  := rand.Intn(len(this.random))
    // fmt.Println(r)
    return this.random[r]
}



/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */