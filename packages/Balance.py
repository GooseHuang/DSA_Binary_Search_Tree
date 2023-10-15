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
import Node
import BinarySearchTree

class FrameWork:
    def __init__(self):
        pass

class InfoHub:
    def __init__(self):
        pass

INFO_HUB = InfoHub()

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
    pass


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


def update_node_depth(node):
    if node.left and node.right:
        node.min_depth = min(node.left.min_depth, node.right.min_depth) + 1
        node.max_depth = max(node.left.max_depth, node.right.max_depth) + 1
    elif node.left:
        node.min_depth = 0
        node.max_depth = node.left.max_depth + 1
    elif node.right:
        node.min_depth = 0
        node.max_depth = node.right.max_depth + 1
    else:
        node.min_depth = 0
        node.max_depth = 0


def update_chain_depth(node):
    # parent = node.parent
    parent = node
    while parent:
        update_node_depth(parent)

        if parent.max_depth - parent.min_depth >= 2:
            get_balance(parent)

        parent = parent.parent


def get_balance(node):
    if node == None:
        return

    center = node
    # fw = FrameWork()
    # fw.center = center
    # fw.left = center.left
    # fw.right = center.right
    # fw.parent = center.parent


    if center.left and center.right:
        if center.left.max_depth - center.right.min_depth >=2:

            # 2. Get right most from left branch
            left_right_most = get_left_right_most(center)
            parent_left_right_most = left_right_most.parent
            disconnect(parent_left_right_most, left_right_most)
            if left_right_most.left:
                if not parent_left_right_most is center:
                    connect(parent_left_right_most, left_right_most.left)
                else:
                    update_node_depth(parent_left_right_most)

            # Update
            update_chain_depth(parent_left_right_most)

            # 1. Center to right
            parent_of_center = center.parent
            center_left = center.left
            center_right = center.right

            disconnect(parent_of_center, center)

            new_node = insert(center.value, center_right)

            disconnect(center, center.right)
            disconnect(center, center.left)

            # Update
            res_node = update_chain_depth(new_node)
            if res_node:
                center_right = res_node

            # 3. Replace center with left right most
            connect(parent_of_center, left_right_most)
            if center_left:
                connect(left_right_most, center_left)
            if center_right:
                connect(left_right_most, center_right)

            # Update
            update_chain_depth(left_right_most)

            if center is INFO_HUB.bst.root:
                INFO_HUB.bst.root = left_right_most


        elif center.right.max_depth - center.left.min_depth >=2:

            # 2. Get left most from right branch

            right_left_most = get_right_left_most(center)
            parent_right_left_most = right_left_most.parent
            disconnect(parent_right_left_most, right_left_most)

            if right_left_most.right:
                if not parent_right_left_most is center:
                    connect(parent_right_left_most, right_left_most.right)
                else:
                    update_node_depth(parent_right_left_most)


            # Update
            update_chain_depth(parent_right_left_most)

            # 1. Center to left
            parent_of_center = center.parent
            disconnect(parent_of_center, center)

            new_node = insert(center.value, center.left)

            center_left = center.left
            center_right = center.right

            disconnect(center, center.right)
            disconnect(center, center.left)

            # Update
            res_node = update_chain_depth(new_node)
            if res_node:
                center_left = res_node



            # 3. Replace center with right left most
            connect(parent_of_center, right_left_most)
            if center_left:
                connect(right_left_most, center_left)
            if center_right:
                connect(right_left_most, center_right)

            # Update
            update_chain_depth(right_left_most)

            if center is INFO_HUB.bst.root:
                INFO_HUB.bst.root = right_left_most
            elif not parent_of_center:
                return res_node

        else:
            pass

    elif center.left:
        if center.left.max_depth >=1:

            """
            Situation:
                left branch>2
                No right branch
            
            """

            # 2. Get right most from left branch

            left_right_most = get_left_right_most(center)
            parent_left_right_most = left_right_most.parent
            disconnect(parent_left_right_most, left_right_most)

            if left_right_most.left:
                if not parent_left_right_most is center:
                    connect(parent_left_right_most, left_right_most.left)
                else:
                    update_node_depth(parent_left_right_most)

            # Update
            update_chain_depth(parent_left_right_most)

            # 1. Center to right
            parent_of_center = center.parent
            center_left = center.left
            center_right = center.right

            disconnect(parent_of_center, center)
            # disconnect(center, center.right)
            disconnect(center, center_left)

            new_node = insert(center.value, center_right)

            # Update
            res_node = update_chain_depth(new_node)
            if res_node:
                center_right = res_node
                connect(left_right_most, center_right)

            # 3. Replace center with left right most
            connect(parent_of_center, left_right_most)
            if center_left:
                connect(left_right_most, center_left)
            # connect(left_right_most, center.right)

            # Update
            update_chain_depth(left_right_most)

            if center is INFO_HUB.bst.root:
                INFO_HUB.bst.root = left_right_most
            elif not parent_of_center:
                return res_node

        else:
            pass


    elif center.right:

        if center.right.max_depth >=1:


            # 2. Get left most from right branch

            right_left_most = get_right_left_most(center)
            parent_right_left_most = right_left_most.parent
            disconnect(parent_right_left_most, right_left_most)
            if right_left_most.right:
                if not parent_right_left_most is center:
                    connect(parent_right_left_most, right_left_most.right)
                else:
                    update_node_depth(parent_right_left_most)

            # Update
            if not parent_right_left_most is center:
                update_chain_depth(parent_right_left_most)

            # 1. Center to left
            parent_of_center = center.parent
            center_left = center.left
            center_right = center.right

            disconnect(parent_of_center, center)
            disconnect(center, center_right)
            # disconnect(center, center.left)

            new_node = insert(center.value, right_left_most)
            # Update
            res_node = update_chain_depth(new_node)
            if res_node:
                center_left = res_node
                connect(right_left_most, center_left)

            # 3. Replace center with right left most
            connect(parent_of_center, right_left_most)
            # connect(right_left_most, center.left)
            if center_right:
                connect(right_left_most, center_right)

            # Update
            update_chain_depth(right_left_most)

            if center is INFO_HUB.bst.root:
                INFO_HUB.bst.root = right_left_most
            elif not parent_of_center:
                return res_node

        else:
            pass


    else:
        # raise ValueError('This should not happen.')
        pass

    return


def main():
    bst = BinarySearchTree.BinarySearchTree([1])

    INFO_HUB.bst = bst

    root = bst.root
    new_node = insert(11, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(24, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(27, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(2, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(3, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(15, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(29, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(37, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(0, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(100, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(55, root)
    update_chain_depth(new_node)

    pn(bst.root)
    # pn(new_node)


import ipdb, traceback, sys
if __name__ == '__main__':
    # try:
    #     main()
    # except:
    #     extype, value, tb = sys.exc_info()
    #     traceback.print_exc()
    #     ipdb.post_mortem(tb)
    main()


# if __name__=='__main__':
#     pass
    # import BinarySearchTree
    #
    #
    # node_string = """
    #                 177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890   283
    #               """
    #
    # node_string = """
    #                 177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890  283
    #               """
    #
    # bst = initial_tree(node_string)
    #
    # depth = get_depth(bst.root)
    # print('Depth:', depth)
    #
    # print("\nOriginal:\n")
    # bst.show()
    #
    #
    #
    # root = get_balance(bst.root)
    # if root:
    #     bst.root = root
    #
    #
    # print("Balanced:\n")
    # bst.show()
