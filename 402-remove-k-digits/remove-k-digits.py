class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        if k> n :
            return "0"

        for c in num :
            while len(stack) > 0 and stack[-1] > c and k>0 :
                if stack[-1] != '0' :
                    k-=1
                stack.pop()

            stack.append(c)

        while k!=0 and len(stack)>0:
            stack.pop()
            k-=1
        ans =""
        while len(stack) >0 :
            ans = stack[-1] + ans
            stack.pop()

        itr = 0
        while itr < len(ans) and ans[itr]=='0':
            itr+=1
        
        
        ans = ans[itr:]
        if len(ans) == 0:
            return "0"
        return ans