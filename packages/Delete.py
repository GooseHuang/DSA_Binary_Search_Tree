import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)

from Utils import connect, disconnect, get_left_right_most, get_right_left_most
from Info import print_node
pn = print_node
import Balance


# def delete(value, root):
#
#     node = root
#     if node == None:
#         return
#
#
#     # Matched
#     if node.value == value:
#         parent = node.parent
#         ind = disconnect(parent, node)
#
#         # No supplement
#         if node.left == None and node.right == None:
#             return
#
#         # Left node as supplement
#         elif node.left != None:
#
#             left_right_most = get_left_right_most(node)
#             parent_left_right_most = left_right_most.parent
#             disconnect(parent_left_right_most, left_right_most)
#
#             if left_right_most:
#                 if left_right_most.left:
#                     connect(parent_left_right_most, left_right_most.left)
#             else:
#                 left_right_most = parent_left_right_most
#
#             if not node.left is left_right_most:
#                 connect(left_right_most, node.left)
#
#             connect(left_right_most, node.right)
#
#             # Connect parent
#             if ind:
#                 connect(parent, left_right_most)
#             else:
#                 root = left_right_most
#                 return root
#
#         # Right node as supplement if there is no left
#         else:
#
#             right_left_most = get_right_left_most(node)
#             parent_right_left_most = right_left_most.parent
#             disconnect(parent_right_left_most, right_left_most)
#
#             if right_left_most:
#                 if right_left_most.right:
#                     connect(parent_right_left_most, right_left_most.right)
#             else:
#                 right_left_most = parent_right_left_most
#
#             if not node.right is right_left_most:
#                 connect(right_left_most, node.right)
#
#             connect(right_left_most, node.left)
#
#             # Connect parent
#             if ind:
#                 connect(parent, right_left_most)
#             else:
#                 root = right_left_most
#                 return root
#
#     # Smaller
#     elif value < node.value:
#         if node.left:
#             delete(value, node.left)
#         else:
#             return
#
#     # Larger
#     elif value > node.value:
#         if node.right:
#             delete(value, node.right)
#         else:
#             return

# Delete with node return


def delete(value, root):

    node = root
    if node == None:
        return

    # Matched
    if node.value == value:
        parent = node.parent
        ind = disconnect(parent, node)

        # No supplement
        if node.left == None and node.right == None:

            res = Balance.update_chain_depth(parent)

            if res:
                print()

            return

        # Left node as supplement
        elif node.left != None:

            left_right_most = get_left_right_most(node)
            parent_left_right_most = left_right_most.parent
            disconnect(parent_left_right_most, left_right_most)
            Balance.update_node_depth(parent_left_right_most)

            tmp_left = left_right_most.left
            tmp_right = left_right_most.right

            if tmp_left:
                connect(parent_left_right_most, left_right_most.left)
                Balance.update_node_depth(parent_left_right_most)

            if not node.left is left_right_most:
                connect(left_right_most, node.left)
                Balance.update_node_depth(left_right_most)

            connect(left_right_most, node.right)
            Balance.update_node_depth(left_right_most)

            res = Balance.update_chain_depth(left_right_most)
            if res:
                left_right_most = res

            # Connect parent
            if ind:
                connect(parent, left_right_most)
                res = Balance.update_chain_depth(parent)
                # print('left res:', res)
                if res:
                    # pn(res)
                    # print()
                    root = res
                    return root
            else:
                root = left_right_most
                return root

        # Right node as supplement if there is no left
        else:

            right_left_most = get_right_left_most(node)
            parent_right_left_most = right_left_most.parent
            disconnect(parent_right_left_most, right_left_most)
            Balance.update_node_depth(parent_right_left_most)

            if right_left_most.right:
                connect(parent_right_left_most, right_left_most.right)
                Balance.update_node_depth(parent_right_left_most)


            if not node.right is right_left_most:
                connect(right_left_most, node.right)
                Balance.update_node_depth(right_left_most)

            connect(right_left_most, node.left)
            Balance.update_node_depth(right_left_most)

            res = Balance.update_chain_depth(right_left_most)
            if res:
                right_left_most = res



            # Connect parent
            if ind:
                connect(parent, right_left_most)
                res = Balance.update_chain_depth(parent)
                # print('right res:', res)
                if res:
                    # pn(res)
                    root = res
                    return root
            else:
                root = right_left_most
                return root

    # Smaller
    elif value < node.value:
        if node.left:
            root = delete(value, node.left)
            return root
        else:
            return

    # Larger
    elif value > node.value:
        if node.right:
            root = delete(value, node.right)
            return root
        else:
            return



if __name__=='__main__':
    import BinarySearchTree

    bst = BinarySearchTree.BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    bst.show()

    root = delete(7, bst.root)
    if root:
        bst.root = root
    bst.show()

    root = delete(3, bst.root)
    if root:
        bst.root = root
    bst.show()

    root = delete(2, bst.root)
    if root:
        bst.root = root
    bst.show()

    root = delete(4, bst.root)
    if root:
        bst.root = root
    bst.show()


    root = delete(5, bst.root)
    if root:
        bst.root = root
    bst.show()


    print('\nDone!\n')