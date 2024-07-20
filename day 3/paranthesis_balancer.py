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
    
    def peek(self):
         if not self.isEmpty():
              return self.head.data
        

if __name__ == "__main__":
    s = input()

    stack = Stack()
    pair = {'{': '}', '(':')', '[':']'}

    for c in s:
        if c in '([{':
             stack.push(c)
        elif c in ')]}':
            if stack.isEmpty() or pair[stack.pop()] != c:
                print('Not Balanced')
                break
    else:
        if not stack.isEmpty():
             print('Not Balanced')
        else:
            print('Balanced')
        