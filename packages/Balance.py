import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


def get_depth(node):
    if node == None:
        return 0

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    return max(left_depth, right_depth) + 1

def get_balance(node):
    if node == None:
        return

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)


    if abs(left_depth-right_depth) >= 2:
        if left_depth > right_depth:

            # Left moves to right

            left_right_most = ...
            # right_left_most = ...

            disconnect(left_right_most)
            get_balance(node.left)
            insert(node, node.right)
            replace(node, left_right_most)



        else:
            get_balance(node.right)
            right_left_most = ...

        left_right_most = ...
        right_left_most = ...
        pass

    return




if __name__=='__main__':
    import BinarySearchTree

    bst = BinarySearchTree.BinarySearchTree([ 81, 77, 70, 12, 92, 39, 31,
                                              59, 11, 25, 58, 52, 38, 84,
                                              21, 79, 78, 18])


    depth = get_depth(bst.root)
    print('Depth:', depth)
    bst.show()
