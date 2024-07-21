class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(val)
        else:
            self.head = Node(val)

    def display(self):
        curr = self.head
        while (curr):
            print(curr.data, end='')
            if curr.next:
                print(' -> ', end='')
            curr = curr.next
        print()

lst = LinkedList()
for x in '2 1 5 7 6 7 2 3 4 9'.split():
    lst.append(int(x))

sums = {}



for i in range(len(arr)):
    s = 0
    for j in range(i, len(arr)):
        s += arr[j]

        if s not in sums:
            sums[s] = [(i, j)]
        else:
            sums[s].append((i, j))

    
for s, lst in sums.items():
    if len(lst) >= 2:
        print(s, end=' - ')
        for i, j in lst:
            print(arr[i:j+1], end=' ')
        print()
