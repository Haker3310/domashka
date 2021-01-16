import random

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        try:
            return self._stack.pop(0)
        except IndexError:
            return "Очередь пуста."

    def peek(self):
        try:
            return self._stack[self.count() - 1]
        except IndexError:
            return "Очередь пуста."

    def count(self):
        return len(self._stack)

someStack = Stack()

for i in range(random.randint(5, 20)):
    someStack.push(random.randint(0, 100))

for i in range(someStack.count()):
    print(someStack.pop(), end='\nЭтот человек сейчас первый : ')