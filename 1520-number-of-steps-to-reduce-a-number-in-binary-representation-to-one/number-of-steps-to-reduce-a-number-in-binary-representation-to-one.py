class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        n = len(s)
        carry = False
        for i in range(n-1,-1,-1) :
            if i == 0 :
                if s[0] == '0':
                    if carry :
                        return steps
                    return -1
                else :
                    if carry :
                        return steps +  1
                    return steps
            if s[i] == '0' and not carry :                    
                steps+=1
            elif s[i] == '1' and carry :
                steps+=1
                carry = True
            else :
                steps +=2
                carry = True

        return -2