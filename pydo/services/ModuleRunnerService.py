from pydo.graphs.DependencyGraph import DependencyGraph
from pydo.modules import Module
from pydo.services.interfaces import IConfigService
from pydo.services.interfaces.IConfigurableService import IConfigurableService


class ModuleRunnerService(IConfigurableService):
    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def run_all(self, modules: list[Module]):
        self.logger().info("Running modules")
        graph = DependencyGraph(modules)

        for module_wrapper in graph.get_traversal():
            module = module_wrapper.get()
            self.run(module)

    def run(self, module: Module):
        self.logger().info(f"Running module: {module.name}")
        module.run()
