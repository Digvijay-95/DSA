class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack1):
            curr = self.stack1.pop()
            self.stack2.append(curr)
        self.stack1.append(x)

        while len(self.stack2):
            curr = self.stack2.pop()
            self.stack1.append(curr)
        

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        if len(self.stack1):
            return self.stack1[-1]

    def empty(self) -> bool:
        return not len(self.stack1)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
obj.push(7)
obj.push(9)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2,param_3,param_4)