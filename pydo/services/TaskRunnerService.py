from pydo.config.Colors import Colors
from pydo.graphs.DependencyGraph import DependencyGraph
from pydo.services.interfaces import IConfigService
from pydo.services.interfaces.IConfigurableService import IConfigurableService
from pydo.tasks import Task


class TaskRunnerService(IConfigurableService):
    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def run_all(self, tasks: list[Task]):
        self.info(f"Running tasks: {tasks}", Colors.OKGREEN)
        graph = DependencyGraph(tasks)

        for task_wrapper in graph.get_traversal():
            task = task_wrapper.get()
            self.run(task)

    def run(self, task: Task):
        self.info(f"Running task: {task.name}", Colors.OKGREEN)
        task.run()
