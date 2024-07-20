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

def simplify(exp):
    ans = ''
    sign = Stack()
    sign.push('+')

    prev = '+'
    isNeg = False
    for c in exp:
        if c == '(':
            sign.push(prev)
            if sign.peek() == '-':
                isNeg = not isNeg
        elif c == ')':
            if sign.pop() == '-':
                isNeg = not isNeg
        elif c in '+-':
            if not isNeg:
                ans += c
            elif c == '+':
                ans += '-'
            else:
                ans += '+'
        else:
            ans += c

        prev = c
    
    print(ans)
    return ans

     
if __name__ == '__main__':
    exp1 = input()
    exp2 = input()

    # exp1 = 'a+b-(c+d)'
    # exp2 = 'a+b-c-d'

    if (simplify(exp1) == simplify(exp2)):
        print("Yes")
    else:
        print('No')
