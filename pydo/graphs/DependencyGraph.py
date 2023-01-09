from pydo.graphs.DirectedAcyclicGraph import DirectedAcyclicGraph
from pydo.graphs.NodeWrapper import NodeWrapper
from pydo.tasks.Task import Task


class DependencyGraph(DirectedAcyclicGraph):
    def __init__(self, tasks: list[Task]):
        super().__init__()
        for task in tasks:
            source_node = NodeWrapper(task)
            self.nodes.add(source_node)
            for dependency in task.dependencies:
                target_node = NodeWrapper(dependency)
                self.nodes.add(target_node)
                self.add_edge(source_node, target_node)
