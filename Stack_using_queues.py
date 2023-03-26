"""
https://leetcode.com/problems/implement-stack-using-queues/description/
"""

class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty() == False:
            return self.stack.pop()

    def top(self) -> int:
        if self.empty() == False:
            return self.stack[-1]

    def empty(self) -> bool:
        if self.stack:
            return False
        return True

    def print(self):
        print(self.stack)


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.empty())
print(obj.pop())
obj.print()
print(obj.top())
obj.print()
