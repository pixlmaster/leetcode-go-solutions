import "fmt"

type RandomizedSet struct {
    hset map[int]int
    keyset []int
}


func Constructor() RandomizedSet {
    randomisedSet := RandomizedSet{
        hset : make(map[int]int),
        keyset: make([]int,0),
    }
    return randomisedSet
}


func (this *RandomizedSet) Insert(val int) bool {
    _, exists := this.hset[val]
    // does not exist
    if !exists {
        // insert 
        this.hset[val] = len(this.keyset)
        this.keyset = append(this.keyset, val)
        return true
    }
    // already exists
    return false

}


func (this *RandomizedSet) Remove(val int) bool {
    index , exists := this.hset[val]
    // exists
    if exists {
        // swap val with the last element in th keyset
        this.keyset[index] = this.keyset[len(this.keyset)-1]
        // change the index of the swapped element
        this.hset[this.keyset[index]] = index
        // delete the element
        this.keyset = this.keyset[:len(this.keyset)-1]
        delete(this.hset,val)
        return true
    }
    // element did not exist
    return false
}


func (this *RandomizedSet) GetRandom() int {
	// Generate a random integer between 0 and len(hset) -1
	randomInt := rand.Intn(len(this.keyset))

	// Retrieve the corresponding value
	return this.keyset[randomInt]

}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */