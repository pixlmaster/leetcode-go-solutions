func wonderfulSubstrings(word string) int64 {
    n := len(word)
    freq := make(map[int]int64)
    freq[0] = 1
    mask := 0
    var ans int64
    ans=0
    for i:=0 ; i < n ; i++ {
        c := word[i]
        idx := int(c) - int('a')
        mask ^= 1 << idx
        ans += freq[mask]
        for j:=0 ; j<10; j++ {
            look := mask ^(1<<j)
            ans += freq[look]
        }
        freq[mask]++;
    }
    return ans

}