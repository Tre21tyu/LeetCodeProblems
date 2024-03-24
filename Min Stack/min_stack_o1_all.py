class MinStack:

    def __init__(self):
        self.stack = []       
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val) 
        if val < self.stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.stack.pop())

    def pop(self) -> None:
        if self.stack:
            self.stack.remove(-1)
            self.min_stack.remove(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return []

    def getMin(self) -> int:
        return self.min_stack[-1]
