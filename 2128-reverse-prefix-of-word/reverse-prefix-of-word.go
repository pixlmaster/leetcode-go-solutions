func reversePrefix(word string, ch byte) string {
    n := len(word)

    for i:=0 ; i < n ; i++ {
        if ch == word[i] {
            reversed := ""
            for j :=i ; j>=0 ; j-- {
                reversed += string(word[j])
            }
            return reversed + word[i+1:n]
        }
    }
    return word
}

