import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

        self.min_depth = 0
        self.max_depth = 0




if __name__=='__main__':
    node = Node(5)
