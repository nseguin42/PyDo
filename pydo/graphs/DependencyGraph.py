from pydo.graphs.DirectedAcyclicGraph import DirectedAcyclicGraph
from pydo.modules.Module import Module
from pydo.graphs.NodeWrapper import NodeWrapper


class DependencyGraph(DirectedAcyclicGraph):
    def __init__(self, modules: list[Module]):
        super().__init__()
        for module in modules:
            source_node = NodeWrapper(module)
            self.nodes.add(source_node)
            for dependency in module.dependencies:
                target_node = NodeWrapper(dependency)
                self.nodes.add(target_node)
                self.add_edge(source_node, target_node)
