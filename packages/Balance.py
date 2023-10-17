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
    child = None
    while parent:
        update_node_depth(parent)
        cur_parent = parent.parent
        if parent.max_depth - parent.min_depth >= 2:
            res_node = get_balance(parent)
            if res_node:
                if cur_parent:
                    connect(cur_parent, res_node)
                else:
                    return res_node

        parent = cur_parent


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
                    tmp_left = left_right_most.left
                    disconnect(left_right_most, tmp_left)
                    connect(parent_left_right_most, tmp_left)
                else:
                    update_node_depth(parent_left_right_most)

            # Update
            update_chain_depth(parent_left_right_most)

            # 1. Center to right
            parent_of_center = center.parent
            center_left = center.left
            center_right = center.right

            disconnect(parent_of_center, center)
            disconnect(center, center.right)
            disconnect(center, center.left)

            new_node = insert(center.value, center_right)

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
            elif not parent_of_center:
                return left_right_most

        elif center.right.max_depth - center.left.min_depth >=2:

            # 2. Get left most from right branch

            right_left_most = get_right_left_most(center)
            parent_right_left_most = right_left_most.parent
            disconnect(parent_right_left_most, right_left_most)

            if right_left_most.right:
                if not parent_right_left_most is center:
                    tmp_right = right_left_most.right
                    disconnect(right_left_most, tmp_right)
                    connect(parent_right_left_most, tmp_right)
                else:
                    update_node_depth(parent_right_left_most)


            # Update
            update_chain_depth(parent_right_left_most)

            center_left = center.left
            center_right = center.right

            # 1. Center to left
            parent_of_center = center.parent
            disconnect(parent_of_center, center)
            disconnect(center, center.right)
            disconnect(center, center.left)

            new_node = insert(center.value, center_left)

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
                return right_left_most

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
                    tmp_left = left_right_most.left
                    disconnect(left_right_most, tmp_left)
                    connect(parent_left_right_most, tmp_left)
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

            if center_right:
                new_node = insert(center.value, center_right)
                res_node = update_chain_depth(new_node)
                if res_node:
                    center_right = res_node
                    connect(left_right_most, center_right)
            else:
                center_right = Node.Node(center.value)
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
                return left_right_most

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
                    tmp_right = right_left_most.right
                    disconnect(right_left_most, tmp_right)
                    connect(parent_right_left_most, tmp_right)
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
                return right_left_most

        else:
            pass


    else:
        # raise ValueError('This should not happen.')
        pass

    return


def balance_insert(bst, value):
    if not bst.root:
        bst.root = Node.Node(value)
        return
    root = bst.root
    new_node = insert(value, root)
    update_chain_depth(new_node)


def string_to_list(node_string):
    node_list = node_string.strip().split(' ')
    node_list = [float(x) if '.' in x else int(x) for x in node_list if x.strip()]
    return node_list


def main():
    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    for x in [1,2,3,4,5,6,7,8,9,0]:
        balance_insert(bst, x)
    pn(bst.root)

    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890   283
                  """
    node_list = string_to_list(node_string)
    for x in node_list:
        balance_insert(bst, x)
    pn(bst.root)


    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877  421  438  865
                """
    node_list = string_to_list(node_string)
    for x in node_list:
        print('Inserting: ', x)
        if x == 476:
            print()
        balance_insert(bst, x)


    x = 770
    balance_insert(bst, x)
    root = bst.root
    pn(root)




    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855   900  605
                     """
    node_list = string_to_list(node_string)
    for x in node_list:
        print('Inserting: ', x)
        if x == 476:
            print()
        balance_insert(bst, x)


    x = 534
    balance_insert(bst, x)
    root = bst.root
    pn(root)




    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855  900  605  534
                     """
    node_list = string_to_list(node_string)
    for x in node_list:
        print('Inserting: ', x)
        if x == 476:
            print()
        balance_insert(bst, x)
    pn(bst.root)





    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855  900  605  534  927  186  242  796  258  657  271  816  624  547  550  571  288  476
                     """
    node_list = string_to_list(node_string)
    for x in node_list:
        print('Inserting: ', x)
        if x == 476:
            print()
        balance_insert(bst, x)
    pn(bst.root)





    bst = BinarySearchTree.BinarySearchTree()
    INFO_HUB.bst = bst
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855  900  605  534  927  186  242  796  258  657  271  816  624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467  397  181  129  706  662  818  727  564  7  428  162  299  206  577  925  953  453  116  118  886  402  890  283  992  557  337  488  959  98  630  255  298  899  942  87  47  858  311  126  441  716  739  93  632  331  936  168  866  458  33  144  973  478  518  83  745  51  596  327  540  751  300  252  8  802  508  996  442  236  830  230  874  999  35  901  110  354  41  651  205  724  91  92  239  336  979  908  748  878  532  355  279  852  871  994  222  957  759  946  920  974  146  287  124  211  981  281  419  84  573  935  130  30  457  333  966  873  766  170  176  201  861  175  97  123  188  723  980  823  363  627  412  484  420  676  840  282  361  591  238  439  514  212  261  14  180  674  849  688  910  602  447  171  234  99  641  127  847  101  834  967  814  758  932  468  307  560  21  18  426  456  854  120  659  883  437  965  179  382  856  483  423  276  246  157  156  109  393  645  694  491  88  538  687  185  448  754  395  660  610  56  147  729  224  693  831  870  805  629  656  85  365  134  319  710  768  663  850  583  312  882  195  978  592  539  655  887  55  512  20  609  961  137  53  76  931  424  463  675  678  636  108  995  387  827  523  752  986  586  26  328  391  256  828  396  253  929  801  339  290  611  24  207  434  303  572  757  501  343  158  671  104  612  701  619  272  810  418  308  561  647  902  568  590  356  227  615  585  152  777  1  574  987  526  266  364  385  941  416  939  912  563  894  820  719  740  792  559  285  486  764  174  787  794  345  705  151  511  46  79  720  461  445  324  905  81  29  169  265  530  531  524  928  819  59  353  1000  991  359  254  637  891  121  16  37  789  788  71  780  427  594  717  496  431  301  472
                  """
    node_list = string_to_list(node_string)
    for x in node_list:
        print('Inserting: ', x)
        if x == 476:
            print()
        balance_insert(bst, x)
    pn(bst.root)



import ipdb, traceback, sys
if __name__ == '__main__':
    # try:
    #     main()
    # except:
    #     extype, value, tb = sys.exc_info()
    #     traceback.print_exc()
    #     ipdb.post_mortem(tb)
    main()


