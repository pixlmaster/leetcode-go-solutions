class MinStack:

    def __init__(self):
        self.numstack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.numstack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else :
            self.minstack.append(min(val,self.minstack[-1]))
        

    def pop(self) -> None:
        self.numstack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.numstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()