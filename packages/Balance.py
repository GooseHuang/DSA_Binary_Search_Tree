import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)

from Utils import connect, disconnect, get_left_right_most, get_right_left_most
from Insert import insert
from Delete import delete
from Info import print_node

class FrameWork:
    def __init__(self):
        pass

def replace(framework, new_node):
    # print_node(framework.node)

    disconnect(framework.node, framework.left)
    disconnect(framework.node, framework.right)

    connect(new_node, framework.left)
    connect(new_node, framework.right)

    if framework.parent != None:
        disconnect(framework.parent, framework.node)
        connect(framework.parent, new_node)
    else:
        return new_node

def get_shortest_path(node):
    if node == None:
        return 0

    left_depth = get_shortest_path(node.left)
    right_depth = get_shortest_path(node.right)

    return min(left_depth, right_depth) + 1


def get_depth(node):
    if node == None:
        return 0

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    return max(left_depth, right_depth) + 1

def trigger(node):

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    left_shortest = get_shortest_path(node.left)
    right_shortest = get_shortest_path(node.right)

    if right_depth-left_shortest >= 2:
        return 'left'
    elif left_depth-right_shortest >= 2:
        return 'right'
    else:
        return 'balanced'


def get_balance(node):
    if node == None:
        return

    print('node:', node.value, 'depth:', get_depth(node), 'shortest:', get_shortest_path(node))
    print_node(node)






    fw = FrameWork()
    fw.node = node
    fw.left = node.left
    fw.right = node.right
    fw.parent = node.parent



    if abs(left_depth-right_depth) >= 2:
        if left_depth > right_depth:

            # Left moves to right
            parent_left_right_most, left_right_most = get_left_right_most(node.left)
            disconnect(parent_left_right_most, left_right_most)
            if not left_right_most:
                left_right_most = parent_left_right_most
            else:
                tmp = left_right_most.left
                disconnect(left_right_most, tmp)
                connect(parent_left_right_most, tmp)


            center = left_right_most
            print('center:', center.value)

            if center is node.left:
                fw.left = None


            root = replace(fw, center)

            get_balance(center.left)

            if center.right:
                insert(node.value, center.right)
                tmp = get_balance(center.right)
                if tmp:
                    center.right = tmp
            else:
                insert(node.value, center)

            if root:
                return root


        else:
            parent_right_left_most, right_left_most = get_right_left_most(node.right)

            disconnect(parent_right_left_most, right_left_most)
            if not right_left_most:
                right_left_most = parent_right_left_most
            else:
                tmp = right_left_most.right
                disconnect(right_left_most, tmp)
                connect(parent_right_left_most, tmp)

            center = right_left_most
            print('center:', center.value)

            if center is node.right:
                fw.right = None


            root = replace(fw, center)

            get_balance(center.right)

            if center.left:
                insert(node.value, center.left)
                tmp = get_balance(center.left)
                if tmp:
                    center.left = tmp
            else:
                insert(node.value, center)

            if root:
                return root

    else:
        pass

    return




if __name__=='__main__':
    import BinarySearchTree

    bst = BinarySearchTree.BinarySearchTree([ 81, 77, 70, 12, 92, 39, 31,
                                              59, 11, 25, 58, 52, 38, 84,
                                              21, 79, 78, 18])

    bst.show()

    depth = get_depth(bst.root)
    print('Depth:', depth)

    root = get_balance(bst.root)
    if root:
        bst.root = root

    root = get_balance(bst.root)
    if root:
        bst.root = root


    root = get_balance(bst.root)
    if root:
        bst.root = root

    root = get_balance(bst.root)
    if root:
        bst.root = root

    root = bst.root
    get_balance(root.left)

    root = bst.root
    get_balance(root.right)


    root = bst.root
    get_balance(root.right.left)




    bst.show()
