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

    def midpoint(self):
        if not self.head:
            return

        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def reverse(self):
        nxt = None
        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def reverseRange(self, i, j):
        if i >= j:
            return

        curr = self.head
        f_prev = None
        count = 0

        while curr and count < i:
            f_prev = curr
            curr = curr.next
            count += 1
        
        f_curr = curr
        prev = None
        while curr and count < j:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        
        if f_prev:
            f_prev.next = prev
        else:
            self.head = prev
        f_curr.next = curr

    def reverseK(self, k):
        if k <= 0:
            return

        curr = self.head
        f_curr = self.head
        prev = None
        f_prev = None
        
        while curr:
            count = 0
            while curr and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1

            if f_prev:
                f_prev.next = prev
            else:
                self.head = prev
            f_curr.next = curr

            f_prev = f_curr
            f_curr = curr
            

if __name__ == '__main__':
    lst = LinkedList()
    
    for num in input("Enter List Elements: ").split():
        lst.append(int(num))

    # k = int(input("Enter k: "))
    # lst.reverseK(k)
    # lst.display()
    print(lst.midpoint())
        