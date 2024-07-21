class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class PolynomialLinkedList:
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
        degree = len(self) - 1

        while (curr):
            if curr.data:
                if curr.data < 0:
                    print(' - ', end='')
                elif curr != self.head:
                    print(' + ', end='')
                print(abs(curr.data), end='')
                if degree:
                    print(f'x^{degree}', end='')
            
            degree -= 1
            curr = curr.next
        print()

    def read(self, s):
        for x in s.split():
            self.append(int(x))

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        
        return count

    def __add__(self, lst):
        curr1 = self.head
        curr2 = lst.head

        ans = PolynomialLinkedList()

        while curr1:
            ans.append(curr1.data + curr2.data)
            curr1 = curr1.next
            curr2 = curr2.next

        return ans

if __name__ == "__main__":
    poly1 = PolynomialLinkedList()
    poly2 = PolynomialLinkedList()

    poly1.read(input())
    poly2.read(input())

    poly3 = poly1 + poly2

    poly3.display()