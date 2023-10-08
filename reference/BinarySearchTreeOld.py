class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, input_list=[]):
        self.root = None
        self.build(input_list)
    def build(self, input_list):
        for x in input_list:
            self.insert(x)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    def _insert(self, value, node):
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            pass

    def delete(self, value):
        print('delete', value)

        if self.root == None:
            return
        else:
            self._delete(value, None, self.root)

    def _disconnect(self, parent, node):
        if parent == None:
            return ''

        elif node is parent.left:
            parent.left = None
            return 'left'
        else:
            parent.right = None
            return 'right'

    def _delete(self, value, parent, node):
        if node == None:
            return

        if node.value == value:
            res = self._disconnect(parent, node)
            if node.left != None:
                parent_left_right_most, left_right_most = self._left_right_most(node.left)

                if left_right_most:
                    if left_right_most.left:
                        parent_left_right_most.right = left_right_most.left
                else:
                    left_right_most = parent_left_right_most

                if not node.left is left_right_most:
                    left_right_most.left = node.left

                left_right_most.right = node.right

                tmp = left_right_most


            elif node.right != None:
                parent_right_left_most, right_left_most = self._right_left_most(node.right)
                if right_left_most:
                    if right_left_most.right:
                        parent_right_left_most.left = right_left_most.right
                else:
                    right_left_most = parent_right_left_most

                if not node.right is right_left_most:
                    right_left_most.right = node.right

                right_left_most.left = node.left

                tmp = right_left_most
            else:
                return

            if res == 'left':
                parent.left = tmp
            elif res == 'right':
                parent.right = tmp
            else:
                self.root = tmp

            return

        elif value < node.value:
            if node.left:
                self._delete(value, node,  node.left)
            else:
                return

        elif value > node.value:
            if node.right:
                self._delete(value, node, node.right)
            else:
                return

    def _left_right_most(self, node):
        parent = node
        node = node.right
        if not node:
            return parent, node

        while node.right:
            parent = node
            node = node.right

        self._disconnect(parent, node)

        return parent, node

    def _right_left_most(self, node):
        parent = node
        node = node.left
        if not node:
            return parent, node

        while node.left:
            parent = node
            node = node.left

        self._disconnect(parent, node)

        return parent, node


    def search(self, value):
        res = self._search(value, self.root)
        if res:
            return True
        else:
            return False

    def _search(self, value, node):
        if not node:
            return None

        if node.value==value:
            return node
        elif node.value<value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)


    def balance(self):
        pass

    def print_node(self, node=""):
        if not node:
            node = self.root
        hub = [node]
        while(hub):
            n = len(hub)
            i = 0
            while(i<n):
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


def test():
    node_list = """
    5 3 9 7 4 2 1 8   3.5  3.2 3.7 3.6 3.8  3.1  3.3
    """
    node_list = node_list.strip().split(' ')
    node_list = [float(x) if '.' in x else int(x) for x in node_list if x.strip()]
    bst = BinarySearchTree()
    for x in node_list:
        bst.insert(x)

    bst.print_node()
    pass


def main():
    pass



if __name__=='__main__':
    test()

