type stack struct{
    st []byte
    top int
}

func createStack(n int) *stack{
    return &stack{make([]byte,n), 0}
}

func (s *stack)push(val byte) {
    s.st[s.top] = val
    s.top++
}

func (s *stack)pop() {
    s.top--
}

func (s *stack)first() byte {
    return s.st[s.top-1]
}

func (s *stack)empty() bool {
    return s.top == 0
}

func (s *stack)print() {
    fmt.Println("Printing stack")
    for i:=s.top-1 ; i>= 0 ; i-- {
        fmt.Println(string(s.st[i]))
    }
    fmt.Println("Ended")
}


func removeKdigits(num string, k int) string {
    n := len(num)
    st := createStack(n)
    removed := 0
    for i:=0 ;i < n ; i++ {
        curr := num[i]
        for ; !st.empty() && removed < k && st.first() > curr ; {
            st.pop()
            removed++
        }
        st.push(curr)
    }
    

    for ; removed < k ; {
        st.pop()
        removed++
    }

    answer := ""

    for ; !st.empty() ; {
        answer = string(st.first()) + answer
        st.pop()
    }
    if len(answer) == 0 {
        return "0"
    }
    // strip 0s
    n = len(answer)
    for i:=0;i<n;i++ {
        if answer[i]!='0'{
            return answer[i:n]
        }else if i==n-1 {
            return "0"
        }
    }

    return answer

}