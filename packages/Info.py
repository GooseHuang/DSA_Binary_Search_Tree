import sys
import os
FILE_PATH = os.path.dirname(__file__)
os.chdir(FILE_PATH)



def print_node(node=""):
    hub = [node]
    while (hub):
        n = len(hub)
        i = 0
        while (i < n):
            head = hub.pop(0)
            if head:
                print(head.value, end="  ")

                if head.left:
                    hub.append(head.left)
                if head.right:
                    hub.append(head.right)

            else:
                print("    ")

            i += 1
        print()

    print()

