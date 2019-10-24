from src.models.trees.base_tree import BaseNode
from src.models.trees.base_tree import BaseTree


class BinaryTree(BaseTree):

    def add_value(self, value):
        if self.root_node is None:
            self.root_node = BinaryNode(value)
        else:
            self.root_node.add_value(value)

    def search(self, value):
        return self.root_node.search(value)

    def __str__(self):
        return str(self.root_node)


class BinaryNode(BaseNode):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

    def add_value(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryNode(value)
            else:
                self.left.add_value(value)
        elif value == self.value:
            self.count += 1
        else:
            if self.right is None:
                self.right = BinaryNode(value)
            else:
                self.right.add_value(value)

    def search(self, value):
        if value == self.value:
            return value, self.count
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return False

    def __str__(self):
        string = ''
        if self.left is not None:
            string += str(self.left)

        string += super().__str__() + ', '

        if self.right is not None:
            string += str(self.right)

        return string
