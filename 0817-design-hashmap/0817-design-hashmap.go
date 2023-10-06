type MyHashMap struct {
    storage [1000001]int
}


func Constructor() MyHashMap {
    hm := MyHashMap{}
    for i := 0 ; i <= 1000000 ; i ++ {
        hm.storage[i] = -1
    }

    return hm

}


func (this *MyHashMap) Put(key int, value int)  {
    this.storage[key] = value
}


func (this *MyHashMap) Get(key int) int {
    return this.storage[key]
}


func (this *MyHashMap) Remove(key int)  {
    this.storage[key] = -1
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */