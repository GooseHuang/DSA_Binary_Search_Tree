import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)

from Utils import connect, disconnect, get_left_right_most, get_right_left_most
from Insert import insert
from Delete import delete
from Info import print_node
pn = print_node
from RandomTree import initial_tree

class FrameWork:
    def __init__(self):
        pass

def replace(framework, new_node):
    # print_node(framework.node)

    disconnect(framework.center, framework.left)
    disconnect(framework.center, framework.right)

    connect(new_node, framework.left)
    connect(new_node, framework.right)

    if framework.parent != None:
        disconnect(framework.parent, framework.center)
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


    if left_depth-right_shortest >= 2:
        return 'left'
    elif right_depth-left_shortest >= 2:
        return 'right'
    else:
        return 'balanced'


def get_balance(node):
    if node == None:
        return

    print('node:', node.value, 'depth:', get_depth(node), 'shortest:', get_shortest_path(node))
    # print_node(node)

    ind = trigger(node)


    if ind == 'balanced':
        return
    else:
        center = node
        root = ''
        while ind != 'balanced':
            if center.left:
                get_balance(center.left)
            if center.right:
                get_balance(center.right)


            fw = FrameWork()
            fw.center = center
            fw.left = center.left
            fw.right = center.right
            fw.parent = center.parent


            if ind=='left':

                # Left moves to right
                parent_left_right_most, left_right_most = get_left_right_most(center.left)
                disconnect(parent_left_right_most, left_right_most)
                if not left_right_most:
                    left_right_most = parent_left_right_most
                else:
                    tmp = left_right_most.left
                    disconnect(left_right_most, tmp)
                    connect(parent_left_right_most, tmp)


                center = left_right_most
                # print('center:', center.value)

                if center is fw.center.left:
                    fw.left = None

                root = replace(fw, center)

                get_balance(center.left)

                if center.right:
                    insert(fw.center.value, center.right)
                    tmp = get_balance(center.right)
                    if tmp:
                        center.right = tmp
                else:
                    insert(fw.center.value, center)


            elif ind=='right':
                parent_right_left_most, right_left_most = get_right_left_most(center.right)

                disconnect(parent_right_left_most, right_left_most)
                if not right_left_most:
                    right_left_most = parent_right_left_most
                else:
                    tmp = right_left_most.right
                    disconnect(right_left_most, tmp)
                    connect(parent_right_left_most, tmp)

                center = right_left_most
                # print('center:', center.value)

                if center is fw.center.right:
                    fw.right = None

                root = replace(fw, center)

                get_balance(center.right)

                if center.left:
                    insert(fw.center.value, center.left)
                    tmp = get_balance(center.left)
                    if tmp:
                        center.left = tmp
                else:
                    insert(fw.center.value, center)

            if root:
                ind = trigger(root)
            else:
                ind = trigger(center)

        if root:
            return root

    return




if __name__=='__main__':
    import BinarySearchTree



    node_string = """
                    177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890   283  
                  """

    node_string = """
                    177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890  283
                  """


    # node_list = [int(x.strip()) for x in node_string.strip().split() if x.strip()]
    #
    # bst = BinarySearchTree.BinarySearchTree()
    #
    # for x in node_list:
    #     bst.insert(x)
    #     root = get_balance(bst.root)
    #     if root:
    #         bst.root = root

    bst = initial_tree(node_string)

    depth = get_depth(bst.root)
    print('Depth:', depth)

    print("\nOriginal:\n")
    bst.show()



    root = get_balance(bst.root)
    if root:
        bst.root = root


    print("Balanced:\n")
    bst.show()
