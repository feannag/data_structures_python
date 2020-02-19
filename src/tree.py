class Tree:
    class Position:
        """an abstraction representing location of single element"""
        def element(self):
            """return element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """return True if other does not represent the same location"""
            return not(self == other)

    def root(self):
        """return the position of the root of the tree T, or None if T is empty"""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """return True if position p is the root of the tree T"""
        return self.root() == p

    def parent(self, p):
        """return the position of the parent of position p, or None if p is the root of T"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """return the number of children of position p"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """generate an iteration of the children of position p"""
        raise NotImplementedError('must be implemented by subclass')

    def is_leaf(self, p):
        """return True if position p does not have any children"""
        return self.num_children(p) == 0

    def __len__(self):
        """return the total number of positions(and hence elements) that are contained in tree T"""
        raise NotImplementedError('must be implemented by subclass')

    def is_empty(self):
        """return True if tree T does not contain any positions"""
        return len(self) == 0

    def positions(self):
        """generate an iteration of all positions of tree T"""
        pass

    @staticmethod
    def iter(T):
        """generate an iteration of all elements stored within tree T"""


class BinaryTree(Tree):
    def left(self, p):
        """return the position that represents the left child of p, or None if p has no child"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """return the position that represents the right child of p, or None if p has no child"""
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """return the position that represents the siblings of p, or None if p has no sibling"""
        parent_of_p = self.parent(p)
        siblings_of_p = self.children(parent_of_p)

        return siblings_of_p

    def children(self, p):
        """generate an iteration of positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    def __init__(self):
        self.__root = None
        self.__size = 0

    class __Node:
        def __init__(self):
            self.parent = None
            self.left = None
            self.right = None
            self.element = None

    def root(self):
        """return the position of the root of the tree T, or None if T is empty"""
        if self.__root is not None:
            return self.__root
        else:
            raise Exception('tree is empty')

    def add_root(self, e):
        """create a root for an empty tree, storing e as the element and return the position of that root;
        an error occurs if the tree is not empty"""
        if self.__root is None:
            self.__root = self.__Node()
            self.__root.element = e

            self.__size += 1

            return self.__root
        else:
            raise Exception('tree already contains root')

    def add_left(self, p, e):
        """create a new node storing element e, link the node as the left child of position p, and return the
        resulting position; an error occurs if p already has a left child"""

        if p.left is None:
            node = self.__Node()
            node.parent = p
            node.element = e
            p.left = node

            self.__size += 1

            return node
        else:
            raise Exception('p already has a left child')

    def add_right(self, p, e):
        """create a new node storing element e, link the node as the right child of position p, and return the
        resulting position; an error occurs if p already has a right child"""

        if p.right is None:
            node = self.__Node()
            node.parent = p
            node.element = e
            p.right = node

            self.__size += 1

            return node
        else:
            raise Exception('p already has a right child')

    @staticmethod
    def replace(p, e):
        """replace the element stored at position p with element e, and return the previously stored element"""
        if p is not None:
            temp = p.element
            p.element = e
            return temp
        else:
            raise Exception('something went wrong')

    def delete(self, p):
        """remove the node at position p, replacing it with its child, if any, and return the element that had been
        stored at p; an error occurs if p has two children"""
        if p is not None:
            if self.num_children(p) == 2:
                raise Exception('cannot delete p: has two children')
            elif self.num_children(p) == 0:
                if self.left(self.parent(p)) == p:
                    self.parent(p).left = None
                    self.__size -= 1
                elif self.right(self.parent(p)) == p:
                    self.parent(p).right = None
                    self.__size -= 1
                elif self.parent(p) is None:
                    self.__root = None
                    self.__size -= 1
            elif self.num_children(p) == 1:
                if self.left(self.parent(p)) == p:
                    self.parent(p).left = p.left
                    self.__size -= 1
                elif self.right(self.parent(p)) == p:
                    self.parent(p).right = p.right
                    self.__size -= 1
        else:
            raise Exception('something went wrong')

    def attach(self, p, T_one, T_two):
        """attach the internal structure of trees T1 and T2 respectively, as the left and right subtrees of leaf
        position p of T, and reset T1 and T2 to empty trees; an error condition occurs if p is not a leaf"""
        if self.is_leaf(p):
            if T_one is not None:
                t_one = self.__Node()
                t_one.parent = p
                t_one.left = T_one.root().left
                t_one.right = T_one.root().right
                t_one.element = T_one.root().element
                p.left = t_one
                self.__size += T_one.__size

            if T_two is not None:
                t_two = self.__Node()
                t_two.parent = p
                t_two.left = T_two.root().left
                t_two.right = T_two.root().right
                t_two.element = T_two.root().element
                p.right = t_two
                self.__size += T_two.__size
        else:
            raise Exception('cannot attach: p is not leaf')

    def num_children(self, p):
        if p.left is not None:
            if p.right is not None:
                return 2
            else:
                return 1
        else:
            return 0

    def parent(self, p):
        """return the position of the parent of position p, or None if p is the root of T"""

        if p is not None:
            return p.parent
        else:
            return None

    def left(self, p):
        """return the position that represents the left child of p, or None if p has no child"""

        if p is not None:
            return p.left
        else:
            return None

    def right(self, p):
        """return the position that represents the right child of p, or None if p has no child"""

        if p is not None:
            return p.right
        else:
            return None

    def __len__(self):
        """return the total number of positions(and hence elements) that are contained in tree T"""
        return self.__size


def main():
    lbt = LinkedBinaryTree()
    root = lbt.add_root(58)
    left = lbt.add_left(root, 31)
    right = lbt.add_right(root, 90)

    # lbt.replace(root, 60)
    # lbt.delete(left)
    # lbt.delete(right)
    # lbt.delete(root)

    t1 = LinkedBinaryTree()
    r1 = t1.add_root(25)
    l1 = t1.add_left(r1, 12)

    t2 = LinkedBinaryTree()
    r2 = t2.add_root(42)
    l2 = t2.add_left(r2, 36)

    lbt.attach(left, t1, t2)

    t3 = LinkedBinaryTree()
    r3 = t3.add_root(62)
    l3 = t3.add_right(r3, 75)

    lbt.attach(right, t3, None)
    pass


if __name__ == '__main__':
    main()
