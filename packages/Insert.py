import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


import Node

def insert(value, node):
    if value > node.value:
        if node.right == None:
            node.right = Node.Node(value)
        else:
            insert(value, node.right)
    elif value < node.value:
        if node.left == None:
            node.left = Node.Node(value)
        else:
            insert(value, node.left)
    else:
        pass
