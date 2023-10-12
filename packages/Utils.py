import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


def connect(parent, node):
    if parent == None or node == None:
        return

    if node.value > parent.value:
        if parent.right:
            parent.right.parent = None

        parent.right = node
    else:
        if parent.left:
            parent.left.parent = None

        parent.left = node

    node.parent = parent


def disconnect(parent, node):
    if parent == None or node == None:
        return ''

    node.parent = None

    if node is parent.left:
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

    # disconnect(parent, node)

    return parent, node

def get_right_left_most(node):
    parent = node
    node = node.left
    if not node:
        return parent, node

    while node.left:
        parent = node
        node = node.left

    # disconnect(parent, node)

    return parent, node
