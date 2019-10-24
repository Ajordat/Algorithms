from abc import ABC
from abc import abstractmethod
from typing import Optional


class BaseTree(ABC):
    def __init__(self, root=None):
        self.root_node: Optional[BaseNode] = root

    @abstractmethod
    def add_value(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass


class BaseNode(ABC):
    def __init__(self, value):
        self.value = value
        self.count = 1

    @abstractmethod
    def add_value(self, node):
        raise NotImplementedError()

    @abstractmethod
    def search(self, value):
        raise NotImplementedError()

    def __str__(self):
        return f'({self.value}, {self.count})'
