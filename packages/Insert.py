import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


import Node

# # Intert Node
# def insert(value, node):
#     if value > node.value:
#         if node.right == None:
#             node.right = Node.Node(value)
#             node.right.parent = node
#         else:
#             insert(value, node.right)
#     elif value < node.value:
#         if node.left == None:
#             node.left = Node.Node(value)
#             node.left.parent = node
#         else:
#             insert(value, node.left)
#     else:
#         pass


# Insert and return node
def insert(value, node):
    if value > node.value:
        if node.right == None:
            new_node = Node.Node(value)
            node.right = new_node
            new_node.parent = node
        else:
            new_node = insert(value, node.right)
    elif value < node.value:
        if node.left == None:
            new_node = Node.Node(value)
            node.left = new_node
            new_node.parent = node
        else:
            new_node = insert(value, node.left)
    else:
        raise ValueError('Value already exists in the tree.')

    return new_node




if __name__=='__main__':
    import BinarySearchTree

    bst = BinarySearchTree.BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    insert(9, bst.root)
    bst.show()
