import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)
sys.path.append(os.path.join(FILE_PATH,'packages'))

import BinarySearchTree


def test():
    node_list = """
    5 3 9 7 4 2 1 8   3.5  3.2 3.7 3.6 3.8  3.1  3.3
    """
    node_list = node_list.strip().split(' ')
    node_list = [float(x) if '.' in x else int(x) for x in node_list if x.strip()]
    bst = BinarySearchTree.BinarySearchTree()
    for x in node_list:
        bst.insert(x)

    # bst.print_node()
    pass


if __name__ == '__main__':
    test()