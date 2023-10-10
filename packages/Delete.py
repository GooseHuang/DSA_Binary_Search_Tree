import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)

def disconnect(parent, node):
    if parent == None:
        return ''

    elif node is parent.left:
        parent.left = None
        return 'left'
    else:
        parent.right = None
        return 'right'

def get_left_right_most(node):
    parent = node
    node = node.right
    if not node:
        return parent, node

    while node.right:
        parent = node
        node = node.right

    disconnect(parent, node)

    return parent, node

def get_right_left_most(node):
    parent = node
    node = node.left
    if not node:
        return parent, node

    while node.left:
        parent = node
        node = node.left

    disconnect(parent, node)

    return parent, node

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

        # Left as supplement first
        elif node.left != None:
            parent_left_right_most, left_right_most = get_left_right_most(node.left)

            if left_right_most:
                if left_right_most.left:
                    parent_left_right_most.right = left_right_most.left
            else:
                left_right_most = parent_left_right_most

            if not node.left is left_right_most:
                left_right_most.left = node.left

            left_right_most.right = node.right

            tmp = left_right_most

        # Right as supplement second
        else:
            parent_right_left_most, right_left_most = get_right_left_most(node.right)
            if right_left_most:
                if right_left_most.right:
                    parent_right_left_most.left = right_left_most.right
            else:
                right_left_most = parent_right_left_most

            if not node.right is right_left_most:
                right_left_most.right = node.right

            right_left_most.left = node.left

            tmp = right_left_most

        # Connect
        if ind == 'left':
            parent.left = tmp
        elif ind == 'right':
            parent.right = tmp
        else:
            root = tmp
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
