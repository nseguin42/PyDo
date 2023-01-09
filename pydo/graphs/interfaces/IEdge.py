from abc import ABCMeta
from typing import Hashable


class IEdge(metaclass=ABCMeta):
    source: Hashable
    target: Hashable

    def __lt__(self, other):
        return self.source < other.source or self.source == other.source and self.target < other.target

    def __repr__(self):
        return f"{self.source} -> {self.target}"

    def __eq__(self, other):
        return self.source == other.source and self.target == other.target

    def __hash__(self):
        return hash((self.source, self.target))
