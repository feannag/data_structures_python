class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not(self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_empty(self):
        return len(self) == 0

    def positions(self):
        pass


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        pass

    def children(self, p):
        pass

class LinkedBinaryTree(BinaryTree):
    pass
