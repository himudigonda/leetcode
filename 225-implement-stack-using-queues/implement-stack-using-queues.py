class MyStack:

    def __init__(self):
        self.q = deque()
        self.q2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        if not self.q:
            self.q.append(x)
        else:
            while self.q:
                self.q2.append(self.q.popleft())
            self.q.append(x)
            while self.q2:
                self.q.append(self.q2.popleft())
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
