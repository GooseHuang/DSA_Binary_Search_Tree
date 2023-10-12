import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)

from Utils import connect, disconnect, get_left_right_most, get_right_left_most


def delete(value, parent, root):

    node = root
    if node == None:
        return

    # Matched
    if node.value == value:
        ind = disconnect(parent, node)

        # No supplement
        if node.left == None and node.right == None:
            return

        # Left node as supplement
        elif node.left != None:

            parent_left_right_most, left_right_most = get_left_right_most(node.left)
            disconnect(parent_left_right_most, left_right_most)

            if left_right_most:
                if left_right_most.left:
                    connect(parent_left_right_most, left_right_most.left)
            else:
                left_right_most = parent_left_right_most

            if not node.left is left_right_most:
                connect(left_right_most, node.left)

            connect(left_right_most, node.right)

            # Connect parent
            if ind:
                connect(parent, left_right_most)
            else:
                root = left_right_most
                return root

        # Right node as supplement if there is no left
        else:

            parent_right_left_most, right_left_most = get_right_left_most(node.right)
            disconnect(parent_right_left_most, right_left_most)

            if right_left_most:
                if right_left_most.right:
                    connect(parent_right_left_most, right_left_most.right)
            else:
                right_left_most = parent_right_left_most

            if not node.right is right_left_most:
                connect(right_left_most, node.right)

            connect(right_left_most, node.left)

            # Connect parent
            if ind:
                connect(parent, right_left_most)
            else:
                root = right_left_most
                return root

    # Smaller
    elif value < node.value:
        if node.left:
            delete(value, node,  node.left)
        else:
            return

    # Larger
    elif value > node.value:
        if node.right:
            delete(value, node, node.right)
        else:
            return

if __name__=='__main__':
    import BinarySearchTree

    bst = BinarySearchTree.BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    delete(7, None, bst.root)
    bst.show()

    print('\nDone!\n')