from abc import ABCMeta
from typing import Set


class INode(metaclass=ABCMeta):
    targets: Set["INode"]

    def __init__(self):
        self.targets = set()

    def get_next_nodes(self) -> Set['INode']:
        return self.targets
