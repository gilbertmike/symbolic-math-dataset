class BinaryUnaryTree:
    def __init__(self):
        self.root = Node(None)
        self.empty_nodes = [self.root]

    def insert_internal_node(self, position, arity):
        raise NotImplementedError

    def generate_prefix(self):
        raise NotImplementedError

class Node:
    def __init__(self, arity):
        self.arity = arity
        self.children = None

    def convert_binary(self):
        self.arity = 2
        self.children = [None, None]

    def convert_unary(self):
        self.arity = 1
        self.children = [None]

    def convert_leaf(self):
        self.arity = 0
        self.children = None

    def is_binary(self):
        return self.arity == 2

    def is_unary(self):
        return self.arity == 1

    def is_leaf(self):
        return self.arity == 0