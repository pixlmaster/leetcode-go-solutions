func maxScoreWords(words []string, letters []byte, score []int) int {
    n := len(words)
    wFreq , lFreq := freqMap(words, letters)
    // fmt.Println(wFreq,lFreq)

    ans := 0
    total := pow(2,n)
    for i :=0 ; i< total ; i++ {
        temp := i
        itr :=0
        currMap := make([]int,26)
        // fmt.Println(temp)
        for ;temp>0; {
            if temp & 1 ==1 {
                addList(currMap,wFreq[itr])
                // fmt.Println(temp, currMap)
                prune, curr := cmpList(currMap,lFreq,score)
                // fmt.Println(prune,curr)
                if prune {
                    break;
                }
                ans = max(ans,curr)
            }
            itr++
            temp = temp >>1
        }
    }

    return ans

}

func addList(list1 []int, list2 []int) {
    for i:=0 ; i< len(list1) ; i++ {
        list1[i] += list2[i]
    }
}

func cmpList(list1 []int, list2 []int, score []int) (bool,int) {
    ans :=0
    for i:=0 ; i< len(list1) ; i++ {
        if list1[i] > list2[i]{
            return true,-1
        }
        ans += list1[i]*score[i]
    }
    return false, ans
}

func freqMap(words []string, letters []byte) ([][]int, []int) {
    n := len(words)
    wordFreq := make([][]int,n)
    for idx, word := range(words) {
        wordFreq[idx] = make([]int,26)
        for _, char := range(word) {
            wordFreq[idx][ord(char)]++
        }
    }
    letterFreq := make([]int, 26)

    for _, letter := range(letters) {
        letterFreq[ord(rune(letter))]++
    }
    return wordFreq, letterFreq

}

func ord(s rune) int {
    return int(s) - int('a')
}

func pow(a,b int) int {
    return int(math.Pow(float64(a), float64(b)))
}

func max(a,b int) int {
    if a>b {
        return a
    }
    return b
}