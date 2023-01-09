import dataclasses

from graphs.interfaces.INode import INode


@dataclasses.dataclass
class BasicNode(INode):
    name: str

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return "Node " + self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
