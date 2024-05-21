type stack struct{
    st []rune
    ptr int
}

func newStack(n int) *stack{
    return &stack{make([]rune,n),0}
}

func (s *stack) isEmpty() bool {
    if s.ptr == 0{
        return true
    }
    return false
}

func (s *stack) push(val rune) {
    s.st[s.ptr] = val
    s.ptr++
}

func (s *stack) pop() rune {
    val := s.st[s.ptr]
    s.ptr--
    return val
}

func (s *stack) top() rune {
    return s.st[s.ptr-1]
}


func isValid(s string) bool {
    circO := '('
    curlO := '{'
    sqarO := '['
    circC := ')'
    curlC := '}'
    stac := newStack(len(s))
    for _, char := range(s) {
        if char == circO || char == curlO || char == sqarO {
            stac.push(char)
            continue
        }
        if stac.isEmpty(){
            return false
        }
        if char == circC{
            if stac.top() != circO {
                return false
            }
            stac.pop()
        } else if char == curlC{
            if stac.top() != curlO {
                return false
            }
            stac.pop()
        } else {
            if stac.top() != sqarO {
                return false
            }
            stac.pop()
        }
    }
    if !stac.isEmpty(){
        return false
    }
    return true
}