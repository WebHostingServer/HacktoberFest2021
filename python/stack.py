
class Stack:

   def __init__(self,max=10):
       self.max = max
       self.stack = []
       self.tos = -1 #   top of stack

   def push(self,data):
      if len(self.stack) >= self.max - 1:
         raise Exception("Stack is full")
      self.stack.append(data)
      self.tos += 1 
      return self.tos

   def pop(self):
      if self.tos == -1:
         raise Exception("Stack is empty")
      self.tos -= 1
      return self.stack.pop()

   def peek(self):
      if self.tos == -1:
         raise Exception("Stack is empty")
      return self.stack[self.tos]

   def is_empty(self):
      return self.tos == -1

   def is_full(self):
      return self.tos == self.max -1

   def map(self,func):
      return [ func(i) for i in self.stack ]



names = Stack()

print("is empty",names.is_empty())
print('is full',names.is_full())
print('push',names.push('hello'))
print('push',names.push('world'))
print('push',names.push('coding'))
print('peek',names.peek())
print('pop',names.pop())
print('is empty',names.is_empty())
print('is full',names.is_full())
