import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


import BinarySearchTree
import random
def initial_tree(node_string):

    node_list = node_string.strip().split(' ')
    node_list = [float(x) if '.' in x else int(x) for x in node_list if x.strip()]
    bst = BinarySearchTree.BinarySearchTree()
    for x in node_list:
        bst.insert(x)

    return bst

def get_random_tree(n=20):
    res = '  '.join( set([str(random.randint(0, 100)) for x in range(n)]))
    return res
