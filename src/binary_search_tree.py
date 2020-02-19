
class Node:
    def __init__(self, element, left=None, right=None, parent=None):
        self.element = element
        self.left = left
        self.right = right
        self.parent = parent

    def get_element(self):
        return self.element


class BinarySearchTree:
    def __init__(self, root: Node):
        self.root = root
        self.size = 0

    def get_root(self):
        return self.root

    def num_children(self, node: Node):
        if node.left is not None:
            if node.right is not None:
                return 2
            else:
                return 1
        else:
            return 0

    def is_leaf(self, node: Node):
        if self.num_children(node) == 0:
            return True
        else:
            return False

    def add_node(self, element):
        node = Node(element)
        self.__add_node(node, self.root)
        self.size += 1

    def __add_node(self, node: Node, current_node: Node):
        if self.is_leaf(current_node):
            if node.get_element() < current_node.get_element():
                current_node.left = node
            else:
                current_node.right = node
        else:
            if node.get_element() < current_node.get_element():
                if current_node.left is not None:
                    self.__add_node(node, current_node.left)
                else:
                    current_node.left = node
            else:
                if current_node.right is not None:
                    self.__add_node(node, current_node.right)
                else:
                    current_node.right = node

    def pre_order_traversal(self):
        print('preorder traversal:')
        self.__pre_order_traversal(self.root)

    def __pre_order_traversal(self, current_node):
        if current_node is None:
            return
        else:
            print(current_node.get_element())
            self.__pre_order_traversal(current_node.left)
            self.__pre_order_traversal(current_node.right)

    def post_order_traversal(self):
        print('postorder traversal:')
        self.__post_order_traversal(self.root)

    def __post_order_traversal(self, current_node):
        if current_node is None:
            return
        else:
            self.__post_order_traversal(current_node.left)
            self.__post_order_traversal(current_node.right)
            print(current_node.get_element())

    def in_order_traversal(self):
        print('inorder traversal:')
        self.__in_order_traversal(self.root)

    def __in_order_traversal(self, current_node):
        if current_node is None:
            return
        else:
            self.__in_order_traversal(current_node.left)
            print(current_node.get_element())
            self.__in_order_traversal(current_node.right)

    def get_children(self, node: Node):
        nodes_list = []

        if node.left is not None:
            nodes_list.append(node.left)
        if node.right is not None:
            nodes_list.append(node.right)

        return nodes_list

    def breadth_first(self):
        print('breadth first:')

        if self.root is not None:
            print(self.root.get_element())
            nodes_list = self.get_children(self.root)

            i = 0
            while i < self.size:
                for node in nodes_list:
                    print(node.get_element())

                    node_children = self.get_children(node)
                    nodes_list.extend(node_children)

                    i += 1

    def search(self, element):
        if self.__search(element, self.root):
            print(f"{element} found")
        else:
            print(f"{element} not found")

    def __search(self, element, current_node):
        if element == current_node.get_element():
            return True
        elif element < current_node.get_element():
            if not self.is_leaf(current_node):
                return self.__search(element, current_node.left)
        else:
            if not self.is_leaf(current_node):
                return self.__search(element, current_node.right)


def main():
    root = Node(58)
    bst = BinarySearchTree(root)

    bst.add_node(31)
    bst.add_node(25)
    bst.add_node(42)
    bst.add_node(12)
    bst.add_node(36)
    bst.add_node(90)
    bst.add_node(62)
    bst.add_node(75)

    bst.pre_order_traversal()
    bst.post_order_traversal()
    bst.in_order_traversal()
    bst.breadth_first()

    bst.search(75)


if __name__ == '__main__':
    main()
