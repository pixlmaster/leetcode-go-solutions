func isPalindrome(s string) bool {
    result := ""
    n:= len(s)
    for i:=0 ; i< n ; i++ {
        result += validate(s[i])
    }
    // fmt.Println(result)
    n=len(result)
    start := 0
    end:=n-1
    if n <=1{
        return true
    }
    for ;start<=end; {
        if result[start]!=result[end]{
            return false
        }
        start++
        end--
    }
    return true

}

func validate(c byte) string {
    cint := int(c)
    aint := int('a')
    zint := int('z')
    Aint := int('A')
    Zint := int('Z')
    int0 := int('0')
    int9 := int('9')
    diff := aint - Aint
    if (cint >= aint && cint<=zint) || (cint>=int0 && cint <= int9) {
        return string(c)
    } else if cint >=Aint && cint <=Zint{
        return string(byte(cint + diff))
    }
    return ""
}