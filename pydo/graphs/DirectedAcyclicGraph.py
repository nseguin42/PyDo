from typing import Generator, Set

import nographs

from pydo.graphs.interfaces import INode


class DirectedAcyclicGraph:
    nodes: Set[INode] = set()

    def get_traversal(self):
        visited = []
        for source in self.nodes:
            if source not in visited:
                for target in self.resolveBranch(source):
                    if target not in visited:
                        visited.append(target)
                        yield target

    @staticmethod
    def resolveBranch(target: INode) -> Generator[INode, None, None]:
        def next_vertices(node: INode, _):
            return node.get_next_nodes()

        traversal = nographs.TraversalTopologicalSort(next_vertices)
        yield from traversal.start_from(target)

    def add_edge(self, source: INode, target: INode):
        if source == target:
            raise ValueError("Cannot add self-referencing edge")
        source.targets.add(target)
