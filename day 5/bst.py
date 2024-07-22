class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.data} - left:{self.left.data if self.left else None}, right:{self.right.data if self.right else None}'


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        self.root = self.insert_rec(self.root, val)
    
    def insert_rec(self, node, val):
        if node:
            if val < node.data:
                node.left = self.insert_rec(node.left, val)
            else:
                node.right = self.insert_rec(node.right, val)
            return node
        else:
            return Node(val)

    def delete(self, val):
        self.root = self.delete_rec(self.root, val)


    def delete_rec(self, node, val):
        if node:
            if val < node.data:
                node.left = self.delete_rec(node.left, val)
            elif val > node.data:
                node.right = self.delete_rec(node.right, val)
            else:
                if not node.left:
                    temp = node.right
                    del node
                    return temp
                elif not node.right:
                    temp = node.left
                    del node
                    return temp
                else:
                    tmp = node.right
                    while tmp.left:
                        tmp = tmp.left
                    node.data = tmp.data
                    node.right = self.delete_rec(node.right, node.data)
            return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def smallestKth(self, root, k, count=0):
        if root:
            count = self.smallestKth(root.left, k, count)
            count += 1
            if count  == k:
                print(root.data)
            count = self.smallestKth(root.right, k, count)
        
        return count
    
    def largestKth(self, root, k, count=0):
        if root:
            count = self.largestKth(root.right, k, count)
            count += 1
            if count  == k:
                print(root.data)
            count = self.largestKth(root.left, k, count)
        
        return count
    
    def closestK(self, root, k, ans):
        if root:
            ans = self.closestK(root.left, k, ans)
            if abs(root.data - k) < abs(ans - k):
                ans = root.data
            else:
                return ans
            ans = self.closestK(root.right, k, ans)
        return ans
        

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')


if __name__ == "__main__":
    bst = BST()

    inp = '42 23 50 17 30 46 65 11 20 40 60 70'
    # inp = '4 6 7 5 2 1 3'

    for i in inp.split():
        bst.insert(int(i))

    print(bst.closestK(bst.root, 49, 999999))
