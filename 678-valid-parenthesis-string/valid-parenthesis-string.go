type stack struct{
    s []int
    topIdx int
}

func NewStack(n int) *stack {
  st := &stack{}
  st.s = make([]int, n)
  st.topIdx = 0
  return st
}

func (st *stack) push(idx int) {
    st.s[st.topIdx] = idx
    st.topIdx++
}

func (st *stack) pop() {
    if(st.topIdx<=0){
        return
    }
    st.topIdx--
}

func (st *stack) top() int {
    if (st.topIdx<=0){
        return -1
    }
    return st.s[st.topIdx-1]
}

func checkValidString(s string) bool {
    n := len(s)
    parStack := NewStack(n)
    strStack :=  NewStack(n)
    openPar := byte('(')
    closePar := byte(')')
    star := byte('*')

    for i:=0 ;i < n ;i++ {
        by := s[i]
        if by == openPar{
            parStack.push(i)
        } else if by == star{
            strStack.push(i)
        } else if by == closePar {
            if parStack.top() != -1 {
                parStack.pop()
            } else if strStack.top() != -1 {
                strStack.pop()
            } else {
                return false
            }
        }
    }

    for ; parStack.top()!=-1 ; {
        parIdx := parStack.top()
        charIdx := strStack.top()
        if charIdx!=-1 && charIdx > parIdx {
            strStack.pop()
            parStack.pop()
        } else{
            return false
        }
    }
    return true

}