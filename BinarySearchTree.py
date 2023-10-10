import sys
import os
FILE_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(FILE_PATH,'packages'))

import Node
import Insert
import Delete
import Info

os.chdir(FILE_PATH)

class BinarySearchTree:
    def __init__(self, input_list=[]):
        self.root = None
        self.build(input_list)
    def build(self, input_list):
        for x in input_list:
            self.insert(x)

    def insert(self, value):
        if self.root is None:
            self.root = Node.Node(value)
        else:
            Insert.insert(value, self.root)

    def delete(self, value):
        print('Delete:', value)

        if self.root == None:
            return
        else:
            root = Delete.delete(value, None, self.root)
            if root:
                self.root = root


    def show(self):
        Info.print_node(self.root)


if __name__=='__main__':
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    bst.delete(5)
    bst.show()

