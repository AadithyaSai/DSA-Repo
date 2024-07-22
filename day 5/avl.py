class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.data} - left:{self.left.data if self.left else None}, right:{self.right.data if self.right else None}'


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, node):
        x = node.left
        y = x.right
        x.right = node
        node.left = y

        return x

    def left_rotate(self, node):
        x = node.right
        y = x.left
        x.left = node
        node.right = y

        return x
    
    
    def insert(self, val):
        self.root = self.insert_rec(self.root, val)
    
    def insert_rec(self, node, val):
        if node:
            if val < node.data:
                node.left = self.insert_rec(node.left, val)
            else:
                node.right = self.insert_rec(node.right, val)

            bf = self.balance_factor(node)
            if bf <= -2:
                if self.balance_factor(node.right) >= 0:
                    node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
            elif bf >= 2:
                if self.balance_factor(node.left) <= 0:
                    node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
            return node
        else:
            return Node(val)
        
    # def delete(self, val):
    #     self.root = self.delete_rec(self.root, val)

    # def delete_rec(self, node, val):
    #     if node:
    #         if val < node.data:
    #             node.left = self.delete_rec(node.left, val)
    #         elif val > node.data:
    #             node.right = self.delete_rec(node.right, val)
    #         else:
    #             if not node.left:
    #                 temp = node.right
    #                 del node
    #                 return temp
    #             elif not node.right:
    #                 temp = node.left
    #                 del node
    #                 return temp
    #             else:
    #                 tmp = node.right
    #                 while tmp.left:
    #                     tmp = tmp.left
    #                 node.data = tmp.data
    #                 node.right = self.delete_rec(node.right, node.data)

    #         bf = self.balance_factor(node)
    #         if bf <= -2:
    #             if self.balance_factor(node.right) >= 0:
    #                 node.right = self.right_rotate(node.right)
    #             node = self.left_rotate(node)
    #         elif bf >= 2:
    #             if self.balance_factor(node.left) <= 0:
    #                 node.left = self.left_rotate(node.left)
    #             node = self.right_rotate(node)

    #         return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, self.height(root), self.balance_factor(root))
            self.inorder(root.right)


if __name__ == "__main__":
    avl = AVL()

    inp = '20 10 30 5 15 '
    # inp = '4 6 7 5 2 1 3'

    for i in inp.split():
        avl.insert(int(i))
        
    avl.inorder(avl.root)

