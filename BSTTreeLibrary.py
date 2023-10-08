import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)
sys.path.append(os.path.join(FILE_PATH,'packages'))

import BinarySearchTree
import Info
def initial_tree(node_string):

    node_list = node_string.strip().split(' ')
    node_list = [float(x) if '.' in x else int(x) for x in node_list if x.strip()]
    bst = BinarySearchTree.BinarySearchTree()
    for x in node_list:
        bst.insert(x)

    return bst


node_string = """
5 3 9 7 4 2 1 8   3.5  3.2 3.7 3.6 3.8  3.1  3.3
"""
bst1 = initial_tree(node_string)

node_string = """
5 3 9 7 4 2 1 8   3.5  3.2 3.7 3.6 3.8  3.1  3.3 58
"""
bst2 = initial_tree(node_string)




if __name__ == '__main__':
    Info.print_node(bst2.root)

    print('Done!')