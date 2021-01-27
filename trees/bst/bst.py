# Original code by : OMKAR PATHAK

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        # Your code goes here
        pass


    def minimum(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        ''' For deleting the node '''
        # Your code goes here
        pass


    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        # Your code goes here
        pass

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self.leftChild:
            self.leftChild.inorder()
        print(str(self.data), end = ' ')
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        # Your code goes here
        pass

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        # Your code goes here
        pass

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        # Your code goes here
        pass

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1)) # should return False
    print(tree.find(12)) # should return True
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    # tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    # tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    # tree.preorder()
