class MyQueue:

    def __init__(self):
        self.mainstack = []
        self.holderstack = []

    def push(self, x: int) -> None:
        self.mainstack.append(x)

    def pop(self) -> int:
        while len(self.mainstack) > 1:
            self.holderstack.append(self.mainstack.pop())
        ret = self.mainstack.pop()
        while self.holderstack:
            self.mainstack.append(self.holderstack.pop())
        return ret        

    def peek(self) -> int:
        while len(self.mainstack) > 1:
            self.holderstack.append(self.mainstack.pop())
        ret = self.mainstack.pop()
        self.mainstack.append(ret)
        while self.holderstack:
            self.mainstack.append(self.holderstack.pop())
        return ret     
        
    def empty(self) -> bool:
        return len(self.mainstack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()