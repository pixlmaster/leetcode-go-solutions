class Solution:
    openPar = "("
    endPar = ")"

    def reverseParentheses(self, s: str) -> str:
        """
        maintain a depth counter, and a stack containing the open positions of the parentheses
        if we counter a closing parentheses and depth is odd -> reverse the stack.top and current position
        else just pop
        """
        stack = deque()
        depth = 0
        sList = list(s)
        for idx, char in enumerate(sList):
            # open paran
            if char == self.openPar:
                stack.append(idx)
                depth += 1
            elif char == self.endPar:
                startIdx = stack.pop()
                sList = self.reverseSubstring(sList, startIdx + 1, idx - 1)
                # print(sList)

                depth -= 1
        ans= ""
        for char in sList:
            if char != self.openPar and char != self.endPar:
                ans+=char
        return ans
        
    def reverseSubstring(self, sList: list[str], start: int, end: int) -> list[str]:
        while start < end:
            temp = sList[start]
            sList[start] = sList[end]
            sList[end] = temp
            start+=1
            end-=1
        return sList