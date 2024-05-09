func reverseWords(s string) string {
    tokens := tokenizer(s)
    ans := ""
    for i:=len(tokens)-1 ; i>= 0 ; i-- {
        ans+= tokens[i]
        if i!=0 {
            ans += " "
        }
    }
    return ans
}

func tokenizer(s string) []string {
    var tokens []string
    token := ""
    n := len(s)
    for i:=0 ; i<n ; i++ {
        if s[i] == ' ' || i==n-1 {
            if s[i] != ' '{
                token += string(s[i])
            }
            if len(token) > 0 {
                tokens = append(tokens, token)
                // fmt.Println("token", token)
                token=""
            }
            continue
        } else{
            token += string(s[i])
        }
    }
    return tokens
}