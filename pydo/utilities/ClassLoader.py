def get_module_class(module_name: str):
    if module_name:
        module = __import__(f"pydo.modules.{module_name}", fromlist=[module_name])
        return getattr(module, module_name)


def get_module_config_class(module_name: str):
    if module_name:
        config_name = module_name + "Config"
        module = __import__(f"pydo.config.{config_name}", fromlist=[config_name])
        return getattr(module, config_name)
