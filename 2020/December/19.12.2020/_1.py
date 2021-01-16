import random

maxcol = 10

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            return "Stack 1 is empty."

    def peek(self):
        try:
            return self._stack[self.count() - 1]
        except IndexError:
            return "Stack 1 is empty."

    def count(self):
        return len(self._stack)

    def newStack(self):
    	class Stack2:
		    def __init__(self):
		        self._stack = []

		    def push(self, x):
		        self._stack.append('Тарелка №',x)

		    def pop(self):
		        try:
		            return self._stack.pop()
		        except IndexError:
		            return "Stack 2 is empty."

		    def peek(self):
		        try:
		            return self._stack[self.count() - 1]
		        except IndexError:
		            return "Stack 2 is empty."

		    def count(self):
		        return len(self._stack)


x = 0
someStack = Stack()

while len[someStack] < maxcol:
	x+=1
    someStack.push(x)
	print(someStack.peek())
	print(someStack.pop())