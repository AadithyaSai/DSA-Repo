class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, val):
            newnode = Node(val)
            newnode.next = self.head
            self.head = newnode
        
    def isEmpty(self):
         return self.head == None
    
    def pop(self):
         if not self.isEmpty():
              tmp = self.head
              val = tmp.data
              self.head = self.head.next
              del tmp
              return val
         
    def display(self):
        tmp = self.head
        
        while tmp:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()
    
    def peek(self):
         if not self.isEmpty():
              return self.head.data
         
def isAlpha(c):
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')

         
if __name__ == '__main__':
    post = input()
    stack = Stack()

    for c in post:
        if isAlpha(c):
            stack.push(c)
        else:
            a = stack.pop()
            b = stack.pop()
            
            stack.push(b+c+a)
    
    stack.display()

    
            
