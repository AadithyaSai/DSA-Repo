class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        curr = self.head
        while (curr):
            print(curr.data, end='')
            if curr.next:
                print(' <-> ', end='')
            curr = curr.next
        print()

    def insertFirst(self, val):
        if self.head:
            tmp = Node(val)
            tmp.next = self.head
            self.head.prev = tmp
            self.head = tmp
        else:
            self.head = Node(val)
            self.tail = self.head

    def insertLast(self, val):
        if self.tail:
            tmp = Node(val)
            tmp.prev = self.tail
            self.tail.next = tmp
            self.tail = tmp
        else:
            self.head = Node(val)
            self.tail = self.head


if __name__ == '__main__':
    lst = DoublyLinkedList()
    
    for num in input("Enter List Elements: ").split():
        lst.insertLast(int(num))

    lst.display()