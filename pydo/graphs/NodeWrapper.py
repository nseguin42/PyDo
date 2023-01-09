from pydo.graphs.interfaces.INode import INode
from pydo.tasks.Task import Task


class NodeWrapper(INode):
    wrapped: Task

    def get(self):
        return self.wrapped

    def __init__(self, wrapped: Task):
        super().__init__()
        self.wrapped = wrapped
        self.targets = set((NodeWrapper(wrapped) for wrapped in wrapped.dependencies))

    def __eq__(self, other):
        return self.wrapped == other.wrapped

    def __hash__(self):
        return hash(self.wrapped)

    def __repr__(self):
        return self.wrapped.__repr__()
