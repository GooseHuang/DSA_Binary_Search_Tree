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
    if not node:
        return None

    if node.left:
        node = node.left

        while node.right:
            parent = node
            node = node.right
        return node

    else:
        return None

def get_right_left_most(node):
    if not node:
        return None

    if node.right:
        node = node.right

        while node.left:
            parent = node
            node = node.left
        return node

    else:
        return None

def get_depth(node):
    if node == None:
        return 0

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    return max(left_depth, right_depth) + 1



def get_shortest_path(node):
    if node == None:
        return 0

    left_depth = get_shortest_path(node.left)
    right_depth = get_shortest_path(node.right)

    return min(left_depth, right_depth) + 1


