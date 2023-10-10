import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)
sys.path.append(os.path.join(FILE_PATH,'packages'))

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



node_string = """
5 3 9 7 4 2 1 8   3.5  3.2 3.7 3.6 3.8  3.1  3.3
"""
print(node_string)

bst1 = initial_tree(node_string)
bst1.show()

print('\n' + '#'*100 + '\n')

node_string = get_random_tree()
print(node_string)
bst2 = initial_tree(node_string)
bst2.show()


"""

"""


if __name__ == '__main__':

    print('Done!')